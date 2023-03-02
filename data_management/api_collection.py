from pandas import read_json
import json
from api_collector import *


# fil = read_json("api_key.json")


# api_key = fil["key"][0]

active_auctions = api_collect_auctions("c2ee8a00-a74e-4f23-802e-a1f1aff1835b", ["Terminator", "Hyperion", "Claymore", "Aspect of the void"])

print(active_auctions)

with open('auctions_info.json', 'w') as outfile:
    json.dump(active_auctions, outfile)

bazaar_info = api_collect_bazaar("c2ee8a00-a74e-4f23-802e-a1f1aff1835b")

with open('bazaar_info.json', 'w') as outfile:
    json.dump(bazaar_info, outfile)

# data = merge_data_json(bazaar_info, active_auctions)

# with open('data.json','w') as outfile:
#     json.dump(data, outfile)