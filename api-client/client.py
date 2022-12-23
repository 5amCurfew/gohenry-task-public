import requests
import json
import pandas as pd
from dotenv import dotenv_values

def callJson(url, headers):
    return json.loads(requests.get(url, headers = headers).text)

class CampaignsAPI(object):
    """Wrapper for the Campaigns API in Python

    Parameters:
        route           String: Route of the desired data from the Campaigns API (e.g. "creatives")
        format          String: format of desired output (either "json" or "DataFrame")
        page            (optional) Integer: initial page number of response. Defaults to 1.
    
    Attributes:
        data            Response data
        current_page    URL of current page

    Methods:
        Next()          Ingest next page of response
        Prev()          Ingest previous page of response
        AppendNext()    Append next page of response data
    """
    def __init__(self, route, format, page = 1):

        self.host = "http://localhost:5000/"
        self.route = route
        self.headers = {
            "Content-Type":"application/json",
            "api_key": dotenv_values(".env")["api_key"]
        }

        self.starting_page = str(page)

        self.last_response_json = callJson(self.host + self.route + "?page=" + self.starting_page, headers = self.headers)
        self.records = json.loads(self.last_response_json["records"])
        
        self.pages = self.last_response_json["links"]
        self.current_page = self.pages[0]["self"]

        self.format = format
        match self.format:
            case "DataFrame":
                self.data = pd.DataFrame(json.loads(self.last_response_json["records"]))
            case _:
                self.data = self.records
    
    def update(self, url):
        self.last_response_json = callJson(url, headers = self.headers)
        self.records = json.loads(self.last_response_json["records"])

        self.pages = self.last_response_json["links"]
        self.current_page = self.pages[0]["self"]

    def Next(self):
        if self.pages[1]["next"] is not None:
            self.update(self.pages[1]["next"])

            match self.format:
                case "DataFrame":
                    self.data = pd.DataFrame(self.records)
                case _:
                    self.data = self.records
        else:
            return
    
    def Prev(self):
        if self.pages[2]["prev"] is not None:
            self.update(self.pages[2]["prev"])

            match self.format:
                case "DataFrame":
                    self.data = pd.DataFrame(self.records)
                case _:
                    self.data = self.records
        else:
            return

    def AppendNext(self):
        if self.pages[1]["next"] is not None:
            self.update(self.pages[1]["next"])

            match self.format:
                case "DataFrame":
                    self.data = pd.concat([self.data, pd.DataFrame(self.records)])
                case _:
                    self.data += self.records
        else:
            return