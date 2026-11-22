
import requests

url = "https://api.ipify.org?format=json"

response = requests.get(url)

print(response)
print(response.status_code)
print(response.text)
print(response.json())
data = response.json()

ip = data["ip"]

print(ip)