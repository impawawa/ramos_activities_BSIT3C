Activity 5

API Documentation
1. Register User
Method: POST

Endpoint URL: /api/register/

Expected Request Body:
{
  "username": "your_name",
  "password": "your_password"
}

Expected Headers:
Content-Type: application/json


Sample Response (Success):
{
  "message": "User registered successfully"
}

Sample Response (Error - Username already exists):
{
  "error": "Username already exists"
}

Sample Response (Error - Missing Fields):
{
  "error": "Username and password required"
}
**********************************************************

2. Login User
Method: POST

Endpoint URL: /api/login/

Expected Request Body:

{
  "username": "john_doe",
  "password": "your_password"
}


Expected Headers:
Content-Type: application/json

Sample Response (Success):
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}

Sample Response (Error - Invalid Credentials):
{
  "detail": "No active account found with the given credentials"
}
*****************************************************************

3. Protected Route (Requires Authentication)
Method: GET

Endpoint URL: /api/protected/

Expected Headers:
Authorization: Bearer <access_token>

Sample Response (Success):
{
  "message": "You are authenticated"
}

Sample Response (Error - Unauthorized):
{
  "detail": "Authentication credentials were not provided"
}
****************************************************************


4. Token Refresh
Method: POST

Endpoint URL: /api/token/refresh/

Expected Request Body:
{
  "refresh": "your_refresh_token"
}
Expected Headers:
Content-Type: application/json

Sample Response (Success):
{
  "access": "your_new_access_token"
}

Sample Response (Error - Invalid Token):
{
  "detail": "Token is invalid or expired"
}
