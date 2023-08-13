### MacTrack

After spending too much time scrolling through [mac.bid](https://mac.bid), I decided it would be a more effective use of my time to write a tool to more effectively use mac.bid.

This webapp aims to achieve 2 goals:
 - notify you when searches matching your criteria are met
 - provide historical data to help inform current purchase decisions

#### Features (WIP)
 - [ ] Automatically updated database of [mac.bid](https://mac.bid) items
   - [x] Manual scraping ability 
 - [x] Full text search via [SQLite's FTS5](https://www.sqlite.org/fts5.html) on over 8 million mac.bid items
 - [ ] Advanced search ability
   - [ ] 2 levels deep boolean logic expressions (eg `(term1 AND term2) OR (term3 AND term4)`)
   - [x] variety of field filters available
 - [ ] Notification on search results via Email, SMS, and more planned in the future


#### Architecture
##### Backend
 - SQLAlchemy for ORM
 - SQLite + FTS5 for DB
##### Frontend
 - React + MUI