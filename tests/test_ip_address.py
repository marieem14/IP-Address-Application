from models.ip_address import IPAddress

def test_ip_address():
    ip = IPAddress(
        ipv4="192.168.1.1",
        ipv6="2001:db8::1",
        country="Tunisia",
        city="Tunis",
        isp="Orange"
    )

    assert ip.get_ipv4() == "192.168.1.1"
    assert ip.get_ipv6() == "2001:db8::1"