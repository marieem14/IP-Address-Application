from utils.ip_validator import is_valid_ipv4, is_valid_ipv6


def test_valid_ipv4():
    assert is_valid_ipv4("192.168.1.1") == True


def test_invalid_ipv4():
    assert is_valid_ipv4("999.999.1.1") == False


def test_valid_ipv6():
    assert is_valid_ipv6("2001:db8::1") == True


def test_invalid_ipv6():
    assert is_valid_ipv6("192.168.1.1") == False