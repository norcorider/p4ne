from flask import Flask, jsonify, render_template
import requests
import json
import pprint


def new_ticket():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    payload = {"username": "devnetuser", "password": "Cisco123!"}
    header = {"content-type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    return response.json()['response']['serviceTicket']


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("topology.html")


@app.route('/api/topology')
def topology():
    return jsonify(responce3.json()['response'])


if __name__ == '__main__':

        ticket = new_ticket()
        controller = "devnetapi.cisco.com/sandbox/apic_em"
        url = "https://" + controller + "/api/v1/host?limit=1&offset=1"
        header = {"content-type": "application/json", "X-Auth-Token": ticket}
        responce = requests.get(url, headers=header, verify=False)
        print("Hosts = ")
#        pprint.pprint(json.dumps(responce.json()))

        url1 = "https://" + controller + "/api/v1/network-device"
        responce2 = requests.get(url1, headers=header, verify=False)
        print("Networkdevices = ")
#       pprint.pprint(json.dumps(responce2.json()))

        url2 = "https://" + controller + "/api/v1/topology/physical-topology"
        responce3 = requests.get(url2, headers=header, verify=False)
        print("Topology = ")
        pprint.pprint(json.dumps(responce3.json()))


app.run(debug=True)

