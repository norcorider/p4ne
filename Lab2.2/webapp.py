from flask import Flask, jsonify
import json
import glob
import re
from ipaddress import *
import pprint

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Main page!"


@app.route('/page1')
def page1():
    return jsonify(host_dict.keys())


@app.route('/page2/<hostname>')
def page2(hostname):
    return jsonify(host_dict[hostname])

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


host_dict = {}


if __name__ == '__main__':
    file_list = glob.glob("C:\\Users\dy.samsonov\seafile\Seafile\p4ne_training\config_files\*.txt")
    for txtdoc in file_list:
         with open(txtdoc) as f:
             current_hostname = ""
             current_iplist = []
             for line in f:
                cache = dyc(line)
                if "hostname" in cache:
                    current_hostname = cache['hostname']
                    print(current_hostname)
                if "ip" in cache:
                    current_iplist.append(str(cache['ip']))
             if current_hostname:
                host_dict[current_hostname] = current_iplist

    app.run(debug=True)
