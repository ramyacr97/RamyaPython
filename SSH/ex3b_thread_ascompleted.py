from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from my_functions import ssh_command2
from my_devices import device_list


if __name__ == "__main__":

    start_time = datetime.now()
    max_threads = 4

    pool = ThreadPoolExecutor(max_threads)

    future_list = []
    for a_device in device_list:
        future = pool.submit(ssh_command2, a_device, "show version")
        future_list.append(future)

    # Process as completed

    for future in as_completed(future_list):
        print("Result: " + future.result())
        end_time = datetime.now()
        print(end_time - start_time)

