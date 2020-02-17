def CalculateNetworkAddress(ip: str,subnet_mask: str) -> str:
    IP_split = ip.split(".")
    subnet_mask = subnet_mask.split(".")
    result = []
    for i in range(len(IP_split)):
        result.append(int(IP_split[i]) & int(subnet_mask[i]))

    res_str = ""
    for nmb in range(len(result)):
        if nmb == 3:
            res_str+=str(result[nmb])
        else:
            res_str+=str(result[nmb])+"."

    return res_str

x = CalculateNetworkAddress("192.168.10.20","255.255.255.0")
print(x)
