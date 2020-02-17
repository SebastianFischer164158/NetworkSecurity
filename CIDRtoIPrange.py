from netaddr import IPNetwork
cidrange = IPNetwork('10.10.15.10/16')
ipstore = [ip for ip in cidrange]
print("-"*20)
print("CIDR to IP Range")
print("-"*20)

print("CIDR Range: ",cidrange)
print("Netmask: ",cidrange.netmask)
print("Wildcard Bits: ",cidrange.hostmask)
print("First IP: ",ipstore[0])
print("Last IP: ",ipstore[-1])
print("Total Host: ",cidrange.size)

print("-"*20)
print("Extra Stuff")
print("-"*20)

print("CIDR prefix bit:\n",cidrange.cidr)
print("CIDR prefix bit:\n",cidrange.netmask.bits())
