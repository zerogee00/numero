#  NUMERO

## Installation:  
`docker run --name numero -d -p 5000:5000 doktorodd/numero`

## Endpoints:

 **`/increment`** - [POST]

Increments how many times the integer in the body has been seen; returns integer

Example: 

> `curl -X POST -H "Content-Type: application/json" -d 1 http://localhost:5000/increment`

Response: 

> `1`

 **`/decrement`** - [POST] ( can only decrement to 0 ) 

Decrements how many times the integer in the body has been seen; returns integer

Example: 

> `curl -X POST -H "Content-Type: application/json" -d 1 http://localhost:5000/decrement`

Response: 200

> `1`

**`/remove`** - [POST]

Removes an item from the data store

Example:

> `curl -X POST -H "Content-Type: application/json" -d 1 http://localhost:5000/remove`

Response: 200

> `1 removed`

**`/history`** - [GET]

Returns all of the existing data

Example: 

> `curl http://localhost:5000/history`

Response: 200 

> `{"1":3,"3":1,"10":3}`

## Errors:

If an item does not exist in the data store and an attempt is made to decrement or remove it a 404 is returned.

**Response: 404**

> `1111111 does not exist`

If an attempt is made to decrement an item that is at 0 a 403 is returned.

**Response: 403**

>`1 would enter negative`
