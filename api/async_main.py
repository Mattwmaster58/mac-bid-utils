import asyncio
from pathlib import Path

import click

from database import init_db_from_engine, create_async_db_config
from scraper.async_updater import MacBidUpdater


async def session_from_db_path(db_path: Path):
    config = create_async_db_config(db_path)
    engine = config.create_engine_callable(config.connection_string)
    await init_db_from_engine(engine)
    return config.create_session_maker()()


async def _update(db_path: Path, skip_correction: bool):
    session = await session_from_db_path(db_path)
    mbc = MacBidUpdater(session)
    if not skip_correction:
        await mbc.correct_auction_groups()
    await mbc.update_locations()
    await mbc.update_buildings()
    await mbc.update_auction_groups()
    await mbc.update_final_auction_lots()
    await mbc.update_live_auction_lots()
    await session.close_all()


@click.command()
@click.option("--db-path", default=Path(__file__).parent / "mac.bid.db", type=click.Path())
@click.option("--skip-correction", default=False, is_flag=True)
def update(db_path: Path, skip_correction: bool):
    db_path = Path(db_path).absolute()
    asyncio.run(_update(db_path, skip_correction))




if __name__ == '__main__':
    update()
