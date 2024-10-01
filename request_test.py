import requests


url = 'http://127.0.0.1:5001/api/login?userID=1'
bodyJson = {
  "Login": "adm",
  "Password": "admk"
}

response = requests.get(url, json = bodyJson)

print(response.text)