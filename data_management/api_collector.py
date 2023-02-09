from requests import get

def api_collect_auctions(api_key):
    response = get("https://api.hypixel.net/skyblock/auctions?key="+api_key)
    temp = response.json()
    auctions = {}
    auctions_id = [temp["auctions"][i]["uuid"] for i in range(len(temp["auctions"]))]
    for id in auctions_id:
            auctions[f"{id}"] = {
                "auctioneer":temp["auctions"][0]["auctioneer"],
                "profile_id":temp["auctions"][0]["profile_id"],
                "coop":temp["auctions"][0]["coop"],
                "start":temp["auctions"][0]["start"],
                "end":temp["auctions"][0]["end"],
                "item_name":temp["auctions"][0]["item_name"],
                "item_lore":temp["auctions"][0]["item_lore"],
                "extra":temp["auctions"][0]["extra"],
                "category":temp["auctions"][0]["category"],
                "tier":temp["auctions"][0]["tier"],
                "starting_bid":temp["auctions"][0]["starting_bid"],
                "item_bytes":temp["auctions"][0]["item_bytes"],
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
        for id in auctions_id:
            auctions[f"{id}"] = {
                "auctioneer":temp["auctions"][i]["auctioneer"],
                "profile_id":temp["auctions"][i]["profile_id"],
                "coop":temp["auctions"][i]["coop"],
                "start":temp["auctions"][i]["start"],
                "end":temp["auctions"][i]["end"],
                "item_name":temp["auctions"][i]["item_name"],
                "item_lore":temp["auctions"][i]["item_lore"],
                "extra":temp["auctions"][i]["extra"],
                "category":temp["auctions"][i]["category"],
                "tier":temp["auctions"][i]["tier"],
                "starting_bid":temp["auctions"][i]["starting_bid"],
                "item_bytes":temp["auctions"][i]["item_bytes"],
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
    

# r1 = api_collect_auctions("02d837e2-0e76-4bb9-a03f-930ef3fda797")

# print(r1)