import threading
from my_functions import ssh_command
from datetime import datetime
from my_devices import device_list


def thread_main():
    start_time = datetime.now()
    threads=[]
    for a_device in device_list:
        my_thread = threading.Thread(target=ssh_command, args=(a_device,"show version"))
        threads.append(my_thread)
        my_thread.start()

    for my_thread in threads:
            my_thread.join()
    end_time = datetime.now()
    print(f"\nElapsed time is {end_time - start_time}")


if __name__ == "__main__":
   thread_main()  
