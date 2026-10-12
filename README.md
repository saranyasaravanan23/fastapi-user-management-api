# User Management REST API

## 1. Project Overview

The User Management REST API is developed using Python, FastAPI, SQLAlchemy, and SQLite. It allows users to create, view, update, and delete user records through REST API endpoints.

## 2. Technologies Used

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn
- Swagger UI

## 3. Features

- Create a new user
- Retrieve all users
- Retrieve a user by ID
- Update user details
- Delete a user
- Filter users by city
- Filter users by active status
- Validate email addresses
- Validate age between 18 and 60
- Prevent duplicate email addresses
- Handle errors for users who do not exist

## 4. Database Fields

| Field | Description |
|---|---|
| id | Unique user ID |
| name | User's name |
| email | Unique email address |
| age | User's age (18–60) |
| city | User's city |
| is_active | Active status |

## 5. API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/users` | Create a user |
| GET | `/users` | Retrieve all users |
| GET | `/users/{user_id}` | Retrieve a user by ID |
| PUT | `/users/{user_id}` | Update user details |
| DELETE | `/users/{user_id}` | Delete a user |

### Optional Filters

- `/users?city=Coimbatore`
- `/users?is_active=true`

## 6. Installation and Execution

1. Install Python.
2. Create and activate a virtual environment.
3. Install dependencies using `pip install -r requirements.txt`.
4. Start the application using `python -m uvicorn main:app --reload`.
5. Open `http://127.0.0.1:8000/docs` to test the API.

The SQLite database is created automatically when the application starts.

## 7. Validation and Error Handling

- `201 Created` — User created successfully.
- `200 OK` — Request completed successfully.
- `404 Not Found` — User does not exist.
- `409 Conflict` — Email address already exists.
- `422 Unprocessable Entity` — Invalid email or age validation failure.

## 8. Testing Results

The following tests were performed using Swagger UI:

- Create user
- Retrieve all users
- Retrieve user by ID
- Update user
- Delete user
- Filter users by city and active status
- Invalid email validation
- Age validation
- Duplicate email validation
- User not found validation

## 9. Conclusion

The User Management REST API provides CRUD operations, database integration, filtering, validation, and error handling. Swagger UI makes it easy to test and verify the API endpoints.