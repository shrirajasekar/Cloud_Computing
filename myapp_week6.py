from flask import Flask, render_template, request, jsonify
import plotly.graph_objs as go
from plotly.utils import PlotlyJSONEncoder
import json
import requests
from pprint import pprint
import requests_cache

requests_cache.install_cache('air_api_cache' , backend= 'sqlite' , expire_after=36000)

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')
app.config['MY_API_KEY']
MY_API_KEY=app.config['MY_API_KEY']

air_url_template = 'https://api.breezometer.com/air-quality/v2/forecast/hourly?lat={lat}&lon={lng}&key={API_KEY}&start_datetime={start}&end_datetime={end}'

@app.route( '/airqualitychart', methods=['GET'])

def airchart():
    my_latitude = request.args.get('lat' , '48.857456')
    my_longitude = request.args.get('lng' , '2.354611' )
    my_start = request.args.get('start' , '2019-02-27T10:00:00')
    my_end = request.args.get('end' , '2019-02-27T12:00:00' )
    air_url = air_url_template.format(lat=my_latitude, lng=my_longitude, API_KEY=MY_API_KEY, start=my_start, end=my_end)
    print(air_url)
    resp = requests.get(air_url)
    if resp.ok:
        resp = requests.get(air_url)
        pprint(resp.json())
    else:
        print(resp.reason)
    return ("Done!")
if __name__=="__main__":
    app.run(port=8080, debug=True)
