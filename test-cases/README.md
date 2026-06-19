# Test Cases
This folder contains my manual testing practice.

## TC001 - Successful user login

| Attribute | Details |
| :--- | :--- |
| **Description** | Verify that a user can successfully log in with valid credentials. |
| **URL / Environment** | `https://practicetestautomation.com/practice-test-login/` |
| **Preconditions** | 1. User has a registered, active account.<br>2. User is on the login page. |
| **Test Data** | Username: `studnet` <br> Password: `Password123` |

### Test Steps
1. Navigate to the login page URL provided above.
2. Enter the valid username into the "Username" field.
3. Enter the valid password into the "Password" field.
4. Click the "Login" button.

### Expected Result
* The user is successfully authenticated and redirected to the user dashboard.
* A welcome message displaying the user's name appears.
