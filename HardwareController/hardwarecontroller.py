import requests

pills = requests.get("http://127.0.0.1:5000/pharmacist/api/get/pills")

print(pills.json())