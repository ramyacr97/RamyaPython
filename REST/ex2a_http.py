import requests
from pprint import pprint

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Constants
BASE_URL = "https://netbox.lasthop.io/api/"

if __name__ == "__main__":
    resp = requests.get(BASE_URL, verify=False)

    print()
    print(f"Response Code: {resp.status_code}")

    print()
    print("Response Text:")
    pprint(resp.text)

    print()
    print("Response JSON:")
    pprint(resp.json())

    print()
    print("Response Headers:")
    pprint(dict(resp.headers))
    print()


