
from services.api_client import APIClient

client = APIClient()

ip = client.get_ipv4()

print("My Public IPv4:", ip)
