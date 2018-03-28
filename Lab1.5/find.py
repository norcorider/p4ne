import glob
import re


ipset = set()
list = (glob.glob("C:\\Users\dy.samsonov\seafile\Seafile\p4ne_training\config_files\*.txt"))
for txtdoc in list:
    with open(txtdoc) as f:
        for line in f:
            if "ip address" in line:
                ipset.add(line)

sortesset = sorted(ipset)

for ipline in sortesset:
    ipline = re.findall(r'[0-9]+(?:\.[0-9]+){3}', ipline)
    if len(ipline) >= 2:
        print(ipline)


m = re.match("^ip address ((?:[0-9]{1,3}\.?){4}) ((?:{0-9]{1,3}\.?){4})", 'ip address 192.168.1.0 255.255.255.0')
