from application.ip_application import IPApplication
from models.ip_address import IPAddress


def test_get_ip_information():

    app = IPApplication()

    ip_info = app.get_ip_information()

    assert isinstance(ip_info, IPAddress)
