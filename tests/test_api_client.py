from unittest.mock import MagicMock, patch
import requests
from services.api_client import APIClient


def test_get_ipv4_success():
    client = APIClient()
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"ip": "102.157.170.87"}

    with patch("services.api_client.requests.get", return_value=mock_response) as mock_get:
        ip = client.get_ipv4()

    assert ip == "102.157.170.87"
    mock_get.assert_called_once()


def test_get_ipv6_returns_none_on_request_error():
    client = APIClient()

    with patch(
        "services.api_client.requests.get",
        side_effect=requests.exceptions.RequestException("Network error"),
    ):
        ipv6 = client.get_ipv6()

    assert ipv6 is None


def test_get_geolocation_invalid_ip_returns_none():
    client = APIClient()
    assert client.get_geolocation("not-an-ip") is None
    assert client.get_geolocation(None) is None


def test_get_geolocation_success():
    client = APIClient()
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "status": "success",
        "city": "Tunis",
        "country": "Tunisia",
        "isp": "Example ISP",
    }

    with patch("services.api_client.requests.get", return_value=mock_response):
        loc = client.get_geolocation("102.157.170.87")

    assert loc == {
        "city": "Tunis",
        "country": "Tunisia",
        "isp": "Example ISP",
    }