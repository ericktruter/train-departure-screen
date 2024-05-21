import os
import requests


def loadDeparturesForStation(journeyConfig, apiKey):
    if journeyConfig["departureStation"] == "":
        raise ValueError(
            "Please set the journey.departureStation property in config.json")

    if apiKey == "":
        raise ValueError(
            "Please complete the transportApi section of your config.json file")

    departureStation = journeyConfig["departureStation"]

    URL = f"https://huxley2.azurewebsites.net/departures/{departureStation}/15"

    PARAMS = {'accessToken': apiKey}

    r = requests.get(url=URL, params=PARAMS)

    data = r.json()

    if "error" in data:
        raise ValueError(data["error"])
    
    return data["trainServices"], data["locationName"]


def loadDestinationsForDeparture(timetableUrl, apiKey):

    URL = f"https://huxley2.azurewebsites.net/service/"+timetableUrl+"/"

    PARAMS = {'accessToken': apiKey}

    r = requests.get(url=URL, params=PARAMS)

    data = r.json()

    if "error" in data:
        raise ValueError(data["error"])
    
    return list(map(lambda x: x["locationName"], data['subsequentCallingPoints'][0]['callingPoint']))[1:]
