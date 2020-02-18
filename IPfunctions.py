from netaddr import IPNetwork, iprange_to_cidrs


def IP_range_to_CIDR(startip: str, endip: str) -> str:

    return str(iprange_to_cidrs(startip, endip)).split("'")[1]

res = IP_range_to_CIDR('10.0.0.0','10.0.0.255')
print("-" * 20)
print("IP Range to CIDR")
print(res)
print("-" * 20)



def CIDRtoIPrange(IPcidr: str):
    cidrange = IPNetwork(IPcidr)
    ipstore = [ip for ip in cidrange]
    print("-" * 20)
    print("CIDR to IP Range")
    print("-" * 20)

    print("CIDR Range: ", cidrange)
    print("Netmask: ", cidrange.netmask)
    print("Wildcard Bits: ", cidrange.hostmask)
    print("First IP: ", ipstore[0])
    print("Last IP: ", ipstore[-1])
    print("Total Host: ", cidrange.size)

    print("-" * 20)
    print("Extra Stuff")
    print("-" * 20)

    print("CIDR prefix bit:",cidrange.cidr)
    print("CIDR prefix bit:",cidrange.netmask.bits())


CIDRtoIPrange('130.255.68.0/22')
