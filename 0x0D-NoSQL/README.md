# 0x0D. NoSQL

## Learning Objectives
- What NoSQL means
- What is difference between SQL and NoSQL
- What is ACID
- What is a document storage
- What are NoSQL types
- What are benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB


## Notes

MongoDB is an open-source document db and the leading NoSQL database, written in C++


### Advantages of MongoDB over RDBMS

- Schema less
- Clear single object structure
- Deep queries, supports dynamic queries
- Tuning
- Easy scalability
- No need to convert application objects to database objects
- Uses internal memory for storing the working set
- Uses *Document Oriented Storage* in JSON style


### Use MongoDB Where...

- You have a ton of data
- A mobile-oriented infrastructure
- You need a hub to access all data


### Data Model Design


#### The Embedded data model

Another word for this is grouped data - like putting all associated data into one dictionary.

```
{
	_id: ,
	ID: "10025AE336"
	Likes: {
		Favorite_Food: "Milk Steak",
        Favorite_Hobby: "Magnets",
		Likes: "Ghouls",
        Interests: "Knees"
	},
	Contact: {
		e-mail: "charlie@gmail.com",
		phone: "5555555555"
	},
	Address: {
		Address: "Paddy's Pub",
		State: "Philadelphia"
	}
}
```


#### The Normalized Data Model

You can refer to sub documents through references.


```
Likes:
{
	_id: <ObjectId101>,
	empDocID: "10025AE336"
    Favorite_Food: "Milk Steak",
    Favorite_Hobby: "Magnets",
    Likes: "Ghouls",
    Interests: "Knees"
}
Contact:
{
    _id: <ObjectId101>,
    e-mail: "charlie@gmail.com",
    phone: "5555555555"
}
Address:
{
    _id: <ObjectId101>,
    Address: "Paddy's Pub",
    State: "Philadelphia"
}
```