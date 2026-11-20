

import requests


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
