from requests import get



def item(i, auctions, temp, id):
    auctions[f"{id}"] = {
        "profile_id":temp["auctions"][i]["profile_id"],
        "start":temp["auctions"][i]["start"],
        "end":temp["auctions"][i]["end"],
        "item_name":temp["auctions"][i]["item_name"],
        "item_lore":temp["auctions"][i]["item_lore"],
        "category":temp["auctions"][i]["category"],
        "tier":temp["auctions"][i]["tier"],
        "starting_bid":temp["auctions"][i]["starting_bid"],
        "claimed":temp["auctions"][i]["claimed"],
        "claimed_bidders":temp["auctions"][i]["claimed_bidders"],
        "highest_bid_amount":temp["auctions"][i]["highest_bid_amount"],
        "bids":temp["auctions"][i]["bids"],
    }

def auctions_constructor(id_list, tracked_items, temp, i):
    for id in id_list:
        for u in range(len(tracked_items)):
            if tracked_items[u] in temp["auctions"][0]["item_name"]:
                item(i, auctions, temp, id)

def api_collect_auctions(api_key, tracked_items):
    response = get("https://api.hypixel.net/skyblock/auctions?key="+api_key)
    temp = response.json()
    auctions = {}
    auctions_id = [temp["auctions"][i]["uuid"] for i in range(len(temp["auctions"]))]
    # auctions_constructor(auctions_id, tracked_items, temp, 0)
    for id in auctions_id:
        for u in range(len(tracked_items)):
            if tracked_items[u] in temp["auctions"][0]["item_name"]:
                item(0,auctions,temp,id)
                auctions[f"{id}"] = {
                    "profile_id":temp["auctions"][0]["profile_id"],
                    "start":temp["auctions"][0]["start"],
                    "end":temp["auctions"][0]["end"],
                    "item_name":temp["auctions"][0]["item_name"],
                    "item_lore":temp["auctions"][0]["item_lore"],
                    "category":temp["auctions"][0]["category"],
                    "tier":temp["auctions"][0]["tier"],
                    "starting_bid":temp["auctions"][0]["starting_bid"],
                    "claimed":temp["auctions"][0]["claimed"],
                    "claimed_bidders":temp["auctions"][0]["claimed_bidders"],
                    "highest_bid_amount":temp["auctions"][0]["highest_bid_amount"],
                    "bids":temp["auctions"][0]["bids"],
                }

    for i in range(1, temp["totalPages"]):
        response = get(f"https://api.hypixel.net/skyblock/auctions?key={api_key}&page={i}")
        temp = response.json()
        auctions_id = [temp["auctions"][i]["uuid"] for i in range(len(temp["auctions"]))]
        i = 0
        # auctions_constructor(auctions_id, tracked_items, temp, i)
        for id in auctions_id:
            for u in range(len(tracked_items)):
                if tracked_items[u] in temp["auctions"][i]["item_name"]:
                    item(i,auctions,temp,id)
                    auctions[f"{id}"] = {
                        "profile_id":temp["auctions"][i]["profile_id"],
                        "start":temp["auctions"][i]["start"],
                        "end":temp["auctions"][i]["end"],
                        "item_name":temp["auctions"][i]["item_name"],
                        "item_lore":temp["auctions"][i]["item_lore"],
                        "category":temp["auctions"][i]["category"],
                        "tier":temp["auctions"][i]["tier"],
                        "starting_bid":temp["auctions"][i]["starting_bid"],
                        "claimed":temp["auctions"][i]["claimed"],
                        "claimed_bidders":temp["auctions"][i]["claimed_bidders"],
                        "highest_bid_amount":temp["auctions"][i]["highest_bid_amount"],
                        "bids":temp["auctions"][i]["bids"],
                    }
        i+=1
    return auctions
            


def api_collect_bazaar(api_key):
    response = get("https://api.hypixel.net/skyblock/bazaar?key="+api_key)
    return response.json()
    

def merge_data_json(col1, col2):
    x = {"bazaar":col1, "auctions":col2}
    return x

# r1 = api_collect_auctions("02d837e2-0e76-4bb9-a03f-930ef3fda797")

# print(r1)