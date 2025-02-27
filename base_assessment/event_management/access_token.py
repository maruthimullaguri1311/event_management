import requests
url = "http://127.0.0.1:8000/auth/token"


data = {
    "username": "testuser",  
    "password": "testpassword" 
}


response = requests.post(url, data=data)


print("Status Code:", response.status_code)
print("Response JSON:", response.json())

if response.status_code == 200:
    # Extract the access token from the response
    token_data = response.json()
    access_token = token_data["access_token"]
    print("Access Token:", access_token)
else:

    print("Failed to get access token:", response.json())