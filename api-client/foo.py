from client import CampaignsAPI

if __name__ == "__main__":
    creatives = CampaignsAPI("creatives", "json")
    campaigns = CampaignsAPI("campaigns", "DataFrame", page = 9)

    print(creatives.current_page)
    print(creatives.data)
    print("--------------------")
    creatives.Next()
    print(creatives.current_page)
    print("--------------------")
    creatives.AppendNext()
    print(creatives.data)
    print("--------------------")
    campaigns.AppendNext()
    print(campaigns.data)
