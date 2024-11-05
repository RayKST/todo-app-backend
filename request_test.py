import requests 


url = 'http://127.0.0.1:5001/api/login'
bodyJson = {
  "Login": "adm",
  "Password": "adm"
}

response = requests.post(url, json = bodyJson)

print(response.text)