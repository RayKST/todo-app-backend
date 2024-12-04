import requests 


url = 'http://127.0.0.1:5001/api/token'
bodyJson = {
  "Username": "adm",
  "Password": "adm"
}
headers = {"Authorization": "Bearer b6b35dea7053cdd2487bd7cc00ce580f"}
response = requests.post(url, json = bodyJson)#, headers=headers)
#response = requests.get(url, headers=headers)
print(response.text)