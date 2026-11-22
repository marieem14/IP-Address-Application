from services.api_client import APIClient
from models.ip_address import IPAddress


class IPApplication:

    def __init__(self):
        self.api_client = APIClient()

    def get_ip_information(self):

        # Get public IPv4
        ipv4 = self.api_client.get_ipv4()

        # Get public IPv6
        ipv6 = self.api_client.get_ipv6()

        # Get geolocation information
        if ipv4:
            location = self.api_client.get_geolocation(ipv4)
        else:
            location = None

        if location is None:
            location = {}

        # Create IPAddress object
        ip_info = IPAddress(
            ipv4=ipv4,
            ipv6=ipv6,
            country=location.get("country"),
            city=location.get("city"),
            isp=location.get("isp")
        )

        return ip_info

    def run(self):

        print("================================")
        print("       IP ADDRESS APPLICATION")
        print("================================")

        ip_info = self.get_ip_information()

        print("\nIP Information:")
        ip_info.display()
