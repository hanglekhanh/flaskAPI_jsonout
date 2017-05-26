import os
from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import requests
import json
import app
app1 = Flask(__name__)

@app1.route('/', methods=['GET', 'POST'])
def index():
   k = app.output_json()
   l = requests.get('http://ip-api.com/json/20.139.146.50')
   return json.dumps(l.json(),indent=2,sort_keys=True)

app1.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

if __name__ == '__main__':
    app1.run()