

import requests
import ipaddress


class APIClient:

    def get_ipv4(self):
        url = "https://api.ipify.org?format=json"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()

            return data["ip"]

        except requests.exceptions.Timeout:
            print("Error: Request timed out.")

        except requests.exceptions.ConnectionError:
            print("Error: No internet connection.")

        except requests.exceptions.HTTPError:
            print("Error: HTTP request failed.")

        except (ValueError, KeyError):
            print("Error: Invalid API response.")

        return None
    def get_ipv6(self):
        url = "https://api6.ipify.org?format=json"    

        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()

            data = response.json()
            return data["ip"]

        except requests.exceptions.RequestException:
            return None
    def get_geolocation(self, ip):
        if not self.is_valid_ip(ip):
            return None

        url = f"http://ip-api.com/json/{ip}"
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            if data.get("status") == "success":
                return {
                    "city": data.get("city"),
                    "country": data.get("country"),
                    "isp": data.get("isp"),
                }
            return None
        except (requests.exceptions.RequestException, ValueError, KeyError):
            return None
    def is_valid_ip(self, ip):
        if not ip:
            return False
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False