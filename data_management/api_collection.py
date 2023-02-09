from pandas import read_json

fil = read_json("api_key.json")
api_key = fil["key"][0]
