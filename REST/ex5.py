import os
import json
import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


# Constants
BASE_URL = "https://netbox.lasthop.io/api/"
ADDRESS_ID = input("Enter Address ID that was created in exercise4: ")

def main():

    token = os.environ["NETBOX_TOKEN"]

    # HTTP POST needs the "Content-Type" header instead of "accept"
    http_headers = {}
    http_headers["Content-Type"] = "application/json; version=2.4;"
    http_headers["accept"] = "application/json; version=2.4;"
    http_headers["Authorization"] = f"Token {token}"

    # Required IP Address data
    data = {"address": "1.1.1.1/32", "description": "Rest API testing"}

    # POST the data to Netbox
    resp = requests.put(
        f"{BASE_URL}ipam/ip-addresses/",
        headers=http_headers,
        verify=False,
        data=json.dumps(data),
    )
    print()
    print(f"Response code: {resp.status_code}")
    print("Returned JSON:")
    print("-" * 12)
    pprint(resp.json())

    # Retrieve the new object ID and query that specific object
    print()
    


if __name__ == "__main__":
    main()
