# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a fully functional REST API using Python's FastAPI framework, learning how to create endpoints, handle path and query parameters, and validate request data with Pydantic models.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Descrição
Set up a FastAPI project and create your first API endpoints. You will build a simple "items" API that returns data in JSON format.

#### Requisitos
O programa concluído deve:

- Import and initialize a `FastAPI` app instance
- Define a `GET /` root endpoint that returns a welcome message, e.g. `{"message": "Welcome to the Items API"}`
- Define a `GET /items` endpoint that returns a hardcoded list of at least 3 items, each with `id` and `name` fields
- Run the app with `uvicorn` and confirm both endpoints respond correctly

**Exemplo de saída esperada para `GET /items`:**
```json
[
  {"id": 1, "name": "Hammer"},
  {"id": 2, "name": "Screwdriver"},
  {"id": 3, "name": "Wrench"}
]
```

### 🛠️ Add Path Parameters and Query Parameters

#### Descrição
Extend your API to support dynamic routes and filtering. You will allow clients to retrieve a specific item by ID and filter items by name using query parameters.

#### Requisitos
O programa concluído deve:

- Define a `GET /items/{item_id}` endpoint that returns the item matching the given `item_id`
- Return a `404` HTTP error with `{"detail": "Item not found"}` if the ID does not exist
- Add an optional query parameter `name` to `GET /items` that filters items whose name contains the given string (case-insensitive)
- Add an optional query parameter `limit` (default: `10`) to `GET /items` that limits the number of items returned

**Exemplo de saída esperada para `GET /items/1`:**
```json
{"id": 1, "name": "Hammer"}
```

**Exemplo de saída esperada para `GET /items?name=screw`:**
```json
[
  {"id": 2, "name": "Screwdriver"}
]
```

### 🛠️ Create and Update Items with Pydantic Models

#### Descrição
Add `POST` and `PUT` endpoints to your API. Use Pydantic models to validate incoming request bodies and store items in an in-memory list.

#### Requisitos
O programa concluído deve:

- Define a Pydantic `BaseModel` class `Item` with fields: `name` (str, required) and `price` (float, required, must be greater than 0)
- Define a `POST /items` endpoint that accepts an `Item` body, assigns it a new unique `id`, appends it to the in-memory list, and returns the created item with status code `201`
- Define a `PUT /items/{item_id}` endpoint that updates an existing item's `name` and `price` by ID
- Return a `404` HTTP error if the item to update does not exist
- Validate that `price` is greater than 0; FastAPI/Pydantic should automatically reject invalid payloads

**Exemplo de payload para `POST /items`:**
```json
{"name": "Pliers", "price": 9.99}
```

**Exemplo de resposta esperada:**
```json
{"id": 4, "name": "Pliers", "price": 9.99}
```
