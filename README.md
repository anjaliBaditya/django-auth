# Django JWT Authentication API

This project demonstrates a simple authentication system using Django Rest Framework and JWT tokens. It includes endpoints for user signup, login, token testing, fetching user details, and an index endpoint.

## Features

- User Signup
- User Login
- JWT Authentication
- Token Verification
- Fetching User Details

## Requirements

- Python 3.6+
- Django 3.0+
- djangorestframework 3.11+
- djangorestframework-simplejwt

## Setup Instructions

Clone the project

```bash
  git clone https://github.com/Arnab-Afk/djangojwt
  cd djangojwt
```


2. Create a Virtual Environment

```bash
  python -m venv venv
  source venv/bin/activate  
  # On Windows, use `venv\Scripts\activate`
```

3. Install Dependencies
```bash
  pip install -r requirements.txt
```

4. Apply Migrations
```bash
  python manage.py migrate
```

5. Run the Development Server
```bash
  python manage.py runserver
```

## API Endpoints

### Signup a New User

```http
  POST /api/signup/
```
Response :

- **Success**: HTTP 200 OK with user data and tokens
- **Failure**: HTTP 400 Bad Request with error details


| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Unique username |
|`password`|`String`|**Required**. Unique password|
|`email`|`string`|**Required**. Unique Email|
---


### Login with an Existing User
```http
  POST /api/login/
```
Response :

- **Success**: HTTP 200 OK with user data and tokens
- **Failure**: HTTP 401 Unauthorized with error details

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Unique username |
|`password`|`String`|**Required**. Unique password|
---
### Index API
```http
  GET /api/index/
  Authorization: Bearer <access_token>
```
Response :

- **Success**: HTTP 200 OK with user data
- **Failure**: HTTP 401 Unauthorized with error details

### Example Unauthorized Request:
```http
    GET /api/index/
```
___

### Running tests
You can run tests in test.rest file to test the endpoints using a REST client like VSCode REST Client:


```http
### Signup a New User
POST /api/signup/
Content-Type: application/json

{
  "username": "testuser",
  "password": "testpassword",
  "email": "testuser@example.com"
}

### Login with the New User
POST /api/login/
Content-Type: application/json

{
  "username": "testuser",
  "password": "testpassword"
}

### Test Token (Replace <access_token> with the token received from the login response)
GET /api/test-token/
Authorization: Bearer <access_token>

### Index API (Replace <access_token> with the token received from the login response)
GET /api/index/
Authorization: Bearer <access_token>

### Index API Unauthorized Access (Without Token)
GET /api/index/
```

---
#### This README should provide a comprehensive guide to setting up and using your Django JWT Authentication API. Feel free to customize it further based on your project's specific needs.