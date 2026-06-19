# API Test Suite: User Authentication API

## Endpoint Overview
* **Base URL:** `https://jsonplaceholder.typicode.com/`
* **Format:** JSON

---

## Test Case 1: Create New User Account (POST /users)

| Attribute | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Path** | `/users` |
| **Description** | Verify a user account is successfully created with valid data. |

### Request Header
```json
{
  "Content-Type": "application/json"
}
