import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv()

load_dotenv()



pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = "blueorange"
TOKEN = os.getenv("token") 


# CREATING AN ACCOUNT USING POST REQUEST, NOTICE WE USED JSON INSTEAD OF PARAMS= WHICH WE USED FOR GET()

pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# action = requests.post(url=pixela_endpoint, json=pixela_params)


# NEXT STEP CREATING, A GRAPH DEFINITION. CALL /V1/USERS/<USERNAME>/GRAPHS BY HTTP POST.
graph_params = {
    "id": "sys5202",
    "name": "My Everyday Writing Graph",
    "unit": "words",
    "type": "int",
    "color": "ajisai",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_action = requests.post(headers=headers, json=graph_params, url=graph_endpoint)

# ADDING A PIXEL TO THE GRAPH
pixelation_header = {
    "X-USER-TOKEN": TOKEN,
}

pixelation_json = {
    "date": datetime.today().strftime("%Y%m%d"),
    "quantity": "219",
}

# /v1/users/<username>/graphs/<graphID>
# pixelation_add = requests.post(url=f"{pixela_endpoint}/{USERNAME}/graphs/sys5202",
#                                json=pixelation_json,
#                                headers=pixelation_header)
print(f"{pixela_endpoint}/{USERNAME}/graphs/sys5202")

# UPDATING AN ALREADY REGISTERED QUANTITY USING PUT
# PUT - /V1/USERS/<USERNAME>/GRAPHS/<GRAPHID>/<YYYYMMDD>
update_header = {
    "X-USER-TOKEN": TOKEN,
}
update_json = {
    "quantity": "417",
}

update_put = requests.put(f"{pixela_endpoint}/{USERNAME}/graphs/sys5202/20250206", json=update_json, headers=update_header)
print(update_put.text)
