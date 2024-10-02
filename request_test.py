import requests 


url = 'http://127.0.0.1:5001/api/login'
bodyJson = {
  "Login": "admin",
  "Password": "adm"
}

response = requests.get(url, json = bodyJson)

print(response.text)