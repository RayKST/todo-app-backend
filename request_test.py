import requests


url = 'http://127.0.0.1:5001/api/task'
bodyJson = {
  "Title": "Teste insert",
  "Description": "tarefona em pai",
  "StartDate": "2024-09-24",
  "EndDate": "2024-10-01"
}

response = requests.post(url, json = bodyJson)

print(response.text)