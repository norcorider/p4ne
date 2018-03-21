from pysnmp.hlapi import *

result = getCmd(SnmpEngine(),
                CommunityData('public', mpModel=0),
                UdpTransportTarget(('10.31.70.107', '161')),
                ContextData(),
                ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

resultList = (list(result))
for i in resultList:
    for n in (i[3]):
        print(n[1])

result2 = nextCmd(
                SnmpEngine(),
                CommunityData('public', mpModel=0),
                UdpTransportTarget(('10.31.70.107', '161')),
                ContextData(),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')), lexicographicMode=False)

result2list=(list(result2))
for i in result2list:
    for n in (i[3]):
        print(n[1])

