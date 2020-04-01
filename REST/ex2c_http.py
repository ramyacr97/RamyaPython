import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Constants
BASE_URL = "https://netbox.lasthop.io/api/"

if __name__ == "__main__":
    print()
    http_headers = {}
    http_headers["accept"] = "application/json; version=2.4;"
    # retrieve /api/dcim
    resp = requests.get(f"{BASE_URL}dcim/", headers=http_headers, verify=False)

    print()
    print("Child endpoint under DCIM")
    pprint(resp.json())


    print()


