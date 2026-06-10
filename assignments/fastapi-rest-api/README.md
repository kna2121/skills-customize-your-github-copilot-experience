# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI by creating endpoints for retrieving and managing data in memory.

## 📝 Tasks

### 🛠️ Create FastAPI endpoints

#### Description
Set up a FastAPI app with routes that return and accept JSON data for a list of items.

#### Requirements
Completed program should:

- Create a FastAPI instance in `main.py`
- Define a `GET /items` endpoint that returns all items
- Define a `GET /items/{item_id}` endpoint that returns a single item by ID
- Return a JSON response with the expected item structure

### 🛠️ Add item creation and validation

#### Description
Implement endpoint logic to add new items and validate incoming request data.

#### Requirements
Completed program should:

- Define a `POST /items` endpoint that accepts JSON data
- Validate that the request contains `name` and `price` fields
- Add new items to an in-memory list and return the created item
- Return a validation error if required fields are missing

### 🛠️ Update and delete items

#### Description
Extend the API to support updating existing items and deleting items by ID.

#### Requirements
Completed program should:

- Define a `PUT /items/{item_id}` endpoint to update an item
- Define a `DELETE /items/{item_id}` endpoint to remove an item
- Return the updated item after a successful update
- Return a meaningful error message if the item ID does not exist
