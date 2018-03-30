import json
import pprint
import re
import requests

with open('card2.json') as jsonfile:
    bankdata = json.load(jsonfile)




#def cardnumber(number):
#    bufnumber = re.match("[0-9]{8}",number)
#    return bufnumber

#pprint.pprint(cardnumber())
#pprint.pprint(bankdata)

card_list = [str(x['CreditCard']['CardNumber'])[0:8] for x in bankdata]


for i in card_list:
    p = requests.get('https://lookup.binlist.net/' + i)
    bankinfa = [n['bank']['name'] for n in p.json()]
    print(bankinfa)

#pprint.pprint(ansfer(json))
#print(card_list)