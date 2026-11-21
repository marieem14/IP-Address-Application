class IPAddress:

    def __init__(self, ipv4=None, ipv6=None, country=None, city=None, isp=None):
        self.ipv4 = ipv4
        self.ipv6 = ipv6
        self.country = country
        self.city = city
        self.isp = isp
    
    def display(self):
        print("IPv4:", self.ipv4)
        print("IPv6:", self.ipv6)
        print("Country:", self.country)
        print("City:", self.city)
        print("ISP:", self.isp)

    def get_ipv4(self):
        return self.ipv4

    def get_ipv6(self):
        return self.ipv6    