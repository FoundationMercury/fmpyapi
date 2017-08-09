"Foundation Mercury Python API Client"

import decimal

import requests


def hello():
    "Hello"
    return "Hello!"

def samples():
    "Samples"
    gets = [
        "/api/census2010/states",
        "/api/census2010/counties/12",
        "/api/census2010/tracts/12/001",
        "/api/census2010/blocks/12/001/000200",
        "/api/census2010/dp/12/001/000301",
        "/api/census2010/sf1basic/state/12/county/097",
        "/api/census2010/zcta5/12",
        "/api/census2010/sf1basic/state/12/zcta5/34746",
        "/api/census2010/sf1basic/state/12/county/001/tract/000301",
        "/api/census2010/sf1basic/state/12/county/001/tract/000200/block/1001",
        "/api/cities/FL",
        "/api/census2010/sf1/01/12/001/000200/1000",
        "/api/census2010/sf1/03/12/001/000200/1000",
        "/api/census2010/sf1/05/12/001/000200/1000",
        "/api/census2010/sf1/06/12/001/000200/1000",
        "/api/census2010/sf1/07/12/001/000200/1000",
        "/api/census2010/sf1/03/docs",
        "/api/geocode/770%20Maple%20Ridge%20Rd,Palm%20Harbor%20FL%2034683",
        "/api/neighborhood/1/census2010/tract",
        "/api/neighborhoods/state/FL/city/Kissimmee",
        "/api/neighborhood/10",
        "/api/revgeocode/28.08893740/-82.75338220"
    ]

URL_BASE = "https://www.foundationmercury.com/api"
    

class CensusState():
    "A US State"
    def __init__(self, d=None):
        self.name = ""
        self.state_abbrev = ""
        self.state_code = ""
        if d:
            self.name = d["name"]
            self.state_abbrev = d["state_abbrev"]
            self.state_code = d["state_code"]


class CensusCounty():
    "A US County or County Equivalent"
    def __init__(self, d=None):
        self.name = ""
        self.county_code = ""
        self.lat = decimal.Decimal(0)
        self.lon = decimal.Decimal(0)
        if d is not None:
            self.name = d["name"]
            self.county_code = d["county_code"]
            self.lat = decimal.Decimal(d["lat"])
            self.lon = decimal.Decimal(d["lon"])


class Client():
    "API Client"

    def __init__(self, username=None, password=None, url_base=None):
        # If these are None, requests will look in .netrc for auth
        self.username = username
        self.password = password
        self.url_base = url_base
        if self.url_base is None:
            self.url_base = URL_BASE


    def get(self, url):
        "Call an API GET endpoint"
        full_url = self.url_base + url
        r = None
        if self.username:
            r = requests.get(full_url, auth=(self.username, self.password))
        else:
            r = requests.get(full_url) # Uses .netrc
        return r.json()
    

    def get_states(self):
        "Get a list of US states"
        j = self.get("/census2010/states")
        states = []
        for d in j:
            states.append(CensusState(d))
        return states


    def get_counties(self, state_code):
        "Get the counties in one state"
        j = self.get("/census2010/counties/" + state_code)
        counties = []
        for d in j:
            counties.append(CensusCounty(d))
        return counties

