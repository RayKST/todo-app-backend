import requests 


url = 'http://127.0.0.1:5001/api/todo_status'
bodyJson = {
  "Username": "adm",
  "Password": "adm"
}
headers = {"Authorization": "Bearer 2627cb2024b98efa3a329afed826423b"}
#response = requests.post(url, json = bodyJson)#, headers=headers)
response = requests.get(url, headers=headers)
print(response.text)