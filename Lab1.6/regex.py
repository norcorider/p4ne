from ipaddress import *
import glob
import re

listip = []
listinterface = []
listhostname = []


def dyc(ip):
    aqip = re.match("^ ip address ((?:[0-9]{1,3}\.?){4}) ((?:[0-9]{1,3}\.?){4})", ip)
    if aqip:
        return {"ip": IPv4Interface(aqip.group(1)+"/"+(aqip.group(2)))}

    aqip = re.match("^interface (.+)", ip)
    if aqip:
        return {"interface": aqip.group(1)}

    aqip = re.match("^hostname (.+)", ip)
    if aqip:
        return {"hostname": aqip.group(1)}
    return {}


#ipset = set()


list = (glob.glob("C:\\Users\dy.samsonov\seafile\Seafile\p4ne_training\config_files\*.txt"))
for txtdoc in list:
    with open(txtdoc) as f:
        for line in f:
            cache = dyc(line)
            if "ip" in cache:
                listip.append(cache)
            if "interface" in cache:
                listinterface.append(cache)
            if "hostname" in cache:
                listhostname.append(cache)

print(listip)
print(listhostname)
print(listinterface)


#for ipline in ipset:
#    ipline = re.match("^interface .+", ipline)
#    if ipline:
#        print(ipline)