# 📘 Assignment: FastAPI REST API

## 🎯 Objective

Build a REST API using the FastAPI framework to practice HTTP methods, path and query parameters, request body validation, and error handling.

## 📝 Tasks

### 🛠️ Initialize the FastAPI Application

#### Description
Create a new FastAPI application and add a basic root endpoint to verify the service is running.

#### Requirements
Completed project should:

- Define a `FastAPI()` application instance.
- Add a root `GET /` endpoint that returns a JSON welcome message.
- Start the app with `uvicorn` for local testing.

### 🛠️ Build CRUD Endpoints for Items

#### Description
Implement endpoints to list items, retrieve a single item by ID, and create new items using request body data.

#### Requirements
Completed project should:

- Define a Pydantic model for item data.
- Add a `GET /items` endpoint to return all items.
- Add a `GET /items/{item_id}` endpoint to return an item by its ID.
- Add a `POST /items` endpoint to create a new item from JSON request data.

### 🛠️ Add Validation and Error Handling

#### Description
Use Pydantic validation and FastAPI error handling to make the API robust.

#### Requirements
Completed project should:

- Validate incoming request bodies with a Pydantic model.
- Return a `404` response when an item ID is not found.
- Return descriptive JSON error messages for invalid input.
