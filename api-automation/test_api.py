
import requests


url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

data = response.json()



print("--- STARTING API TEST ---")

if response.status_code == 200:
    print("✅ Pass: Status code is 200 OK!")
else:
    print(f"❌ Fail: Expected 200, but got {response.status_code}")

expected_name = "Bret"
actual_name = data["username"]

if actual_name == expected_name:
    print(f"✅ Pass: User name is correctly '{actual_name}'!")
else:
    print(f"❌ Fail: Expected '{expected_name}', but got '{actual_name}'")

print("--- TEST COMPLETE ---")