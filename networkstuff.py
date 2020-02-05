

def CalculateNetworkAddress(ip: str,subnetmask: str) -> str:
    IPsplit = ip.split(".")
    subnetmask = subnetmask.split(".")
    result = []
    for i in range(len(IPsplit)):
        result.append(int(IPsplit[i]) & int(subnetmask[i]))

    res_str = ""
    for nmb in range(len(result)):
        if nmb == 3:
            res_str+=str(result[nmb])
        else:
            res_str+=str(result[nmb])+"."

    return res_str

x = CalculateNetworkAddress("192.38.95.89","255.255.255.0")
print(x)
