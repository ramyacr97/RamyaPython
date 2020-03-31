from my_devices import device_list
from my_functions import napalm_connect


if __name__ == "__main__":
    connection = []
    for device in device_list:
        conn = napalm_connect(device)
        connection.append(conn)

    for conn in connection:
        print(conn)
        conn.load_merge_candidate(filename="{}-loopbacks".format(conn.hostname))
        print("Difference in device{}".format(conn.hostname))
        diff = conn.compare_config()
        print(diff)
        if diff:
            conn.commit_config()
            print("Difference in device after commiting{}".format(conn.hostname))
        print(conn.compare_config())
        conn.close()

