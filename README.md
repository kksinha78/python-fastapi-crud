
# Student Management API using FastAPI

This project is a beginner-friendly REST API built with [FastAPI](https://fastapi.tiangolo.com/?utm_source=chatgpt.com) to perform CRUD operations (Create, Read, Update, Delete) on student data.

The API demonstrates:

* FastAPI endpoint creation
* Path parameters
* Query parameters
* Request body handling
* Pydantic models
* POST, GET, PUT, and DELETE methods
* Data validation using Pydantic
* Optional fields for updates

## Features

* Get student details by ID
* Search students by name
* Create a new student
* Update existing student information
* Delete a student record

## Technologies Used

* Python
* [FastAPI](https://fastapi.tiangolo.com/?utm_source=chatgpt.com)
* [Pydantic](https://docs.pydantic.dev/latest/?utm_source=chatgpt.com)

## Run the Application

```bash
fastapi dev myapi.py
```

## API Endpoints

| Method | Endpoint                       | Description         |
| ------ | ------------------------------ | ------------------- |
| GET    | `/`                            | Home endpoint       |
| GET    | `/get-student/{student_id}`    | Get student by ID   |
| GET    | `/get-by-name`                 | Get student by name |
| POST   | `/create-student/{student_id}` | Create new student  |
| PUT    | `/update-student/{student_id}` | Update student      |
| DELETE | `/delete-student/{student_id}` | Delete student      |

## Purpose

This project was created for learning and practicing FastAPI concepts, including API routing, request handling, and CRUD operations.
