from flask import Flask, request
import rivalcfg as rc

import json
app = Flask(__name__)



device = rc.get_first_mouse()

@app.route("/", methods=['GET','POST'])
def main():
    if request.method != 'POST':
        return('done')
    req = request.get_json(silent=True)
    resp = {'fulfillmentText': "Welcome!"}
    try:
        color = req['queryResult']['parameters']['color']
        device.set_color(color)

        resp = {
            "fulfillmentText": "Done!"
            }
    except:
        pass

    return json.dumps(resp)
