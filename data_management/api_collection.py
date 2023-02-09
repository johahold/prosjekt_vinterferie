from pandas import read_json
import json
from api_collector import *

fil = read_json("api_key.json")
api_key = fil["key"][0]

active_auctions = api_collect_auctions(api_key)

with open('auctions_info.json', 'w') as outfile:
    json.dump(active_auctions, outfile)

bazaar_info = api_collect_bazaar(api_key)

with open('bazaar_info.json', 'w') as outfile:
    json.dump(bazaar_info, outfile)

