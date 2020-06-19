# 0x0B. Redis basic

## Notes

### What is Redis?
- Redis is a noSQL key/value store
- can be used as a db or a cache and message broker
- supports many data structures
- built in replication of servers (master/slave relationship)


### Supported data types
- Strings
- Lists
- Sets
- Sorted sets
- Hashes (key/value pairs)
- Bitmaps (based on strings)
- Hyperlogs
- Geospatial indexes


### Advantages
- No schemas and column names
- Super fast! Hundreds of thousands of SETs or GETs per sec
- Like mongoDB and memcache, best of both worlds
- Can be used with pretty much anything


### Redis & Security
- Use internally, dont let access to internet!
- Not supported data encryption
