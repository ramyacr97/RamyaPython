from my_functions import napalm_connect, create_checkpoint
from my_devices import nxos1
from pprint import pprint

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

NXOS_REPLACE_CANDIDATE = "nxos1_replacement_cfg"

if __name__ == "__main__":
    conn = napalm_connect(nxos1)
    create_checkpoint(conn)
    conn.load_replace_candidate(NXOS_REPLACE_CANDIDATE)
    print("config staged {}".format(conn.hostname))
    print(conn.compare_config())
    print("Dsicarding candidate config {}".format(conn.hostname))
    conn.discard_config()
    print("Difference after discard candidate config {}".format(conn.hostname))
    print(conn.compare_config())
    print("\n\n")
    conn.close()

