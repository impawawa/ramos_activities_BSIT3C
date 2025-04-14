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


****************************************************************

To see if you are authenticaded add put this to the powershell


Steps to See if your credentials is Authenticated:
1. Login your Credentials if don't have account create in /register
2. After logging in copy the access token
3. After copying the access token write this in your terminal/powershel and make sure you to put your own access token:

$headers = @{
    "Authorization" = "Bearer your_access_token_here"
}

Invoke-WebRequest -Uri "http://localhost:8000/api/protected/" -Headers $headers

Response:
StatusCode        : 200
StatusDescription : OK
Content           : {"message":"You are authenticated"}
RawContent        : HTTP/1.1 200 OK
                    Vary: Accept
                    Allow: GET, HEAD, OPTIONS
                    X-Frame-Options: DENY
                    X-Content-Type-Options: nosniff
                    Referrer-Policy: same-origin
                    Cross-Origin-Opener-Policy: same-origin
                    Content-Length:...
Forms             : {}
Headers           : {[Vary, Accept], [Allow, GET, HEAD, OPTIONS], [X-Frame-Options, DENY], [X-Content-Type-Options, nosniff]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 35


