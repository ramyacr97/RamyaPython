from concurrent.futures import ProcessPoolExecutor
from datetime import datetime
from my_functions import ssh_command2
from my_devices import device_list

if __name__ == "__main__":

    start_time = datetime.now()
    max_procs = 5
 # Use context manager to clean up
    with ProcessPoolExecutor(max_procs) as pool:

        future_list = []
        for a_device in device_list:
            if "junos" in a_device["device_type"]:
                future_list.append("show arp")
            else:
                future_list.append("show ip arp")
            results = pool.map(ssh_command2, device_list, future_list)
            
        ### Process as completed
            for result in results:
                print(">>>"*40)
                print("Result: ", result)

            end_time = datetime.now()
            print(end_time - start_time)
