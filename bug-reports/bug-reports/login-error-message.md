# Bug Report: No Error Message Displayed for Invalid Password

| Attribute | Details |
| :--- | :--- |
| **Bug ID** | BUG-001 |
| **Severity** | Medium |
| **Status** | Open |
| **Environment** | Chrome v148.0.7778.168 |

## Description
When attempting to log in with a valid username but an incorrect password, the system fails to display any error message to the user, leaving them on a frozen login screen.

## Steps to Reproduce
1. Open the login page.
2. Enter a valid username `testuser@example.com`.
3. Enter an invalid password `WrongPassword123`.
4. Click the **Login** button.

## Expected Result
An error message stating `"Incorrect username or password"` should be displayed in red text below the password field.

## Actual Result
No error message is shown. The page remains unchanged, and there is no visual feedback for the user.
