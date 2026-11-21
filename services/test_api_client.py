
from services.api_client import APIClient

client = APIClient()

ipv4 = client.get_ipv4()

print("Public IPv4:", ipv4)

if ipv4:
    location = client.get_geolocation(ipv4)

    print("\n--- Geolocation ---")

    if location:
        print("City:", location.get("city"))
        print("Country:", location.get("country"))
        print("ISP:", location.get("isp"))
    else:
        print("Geolocation unavailable")