"""testing alembic usage - add approved col on user

Revision ID: 80d38c9c852a
Revises: 
Create Date: 2023-08-09 23:05:27.873002

"""
from contextlib import suppress
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80d38c9c852a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with suppress(Exception):
        op.drop_table('auction_lot_idx')
        op.drop_column('location', 'test_col')
    op.add_column('user', sa.Column('approved', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'approved')
    op.add_column('location', sa.Column('test_col', sa.INTEGER(), nullable=True))
    # don't care about the auction_lot_idx table
    # ### end Alembic commands ###
