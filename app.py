import flask
import json
from pprint import pprint
    
with open('data.json') as data_file:    
    data = json.load(data_file)


def output_json():
    return json.dumps(data,indent=2,sort_keys=True)

