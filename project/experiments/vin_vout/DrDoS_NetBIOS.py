import numpy as nump
import csv
import matplotlib.pyplot as plot


def drdos_netbios_ana(ty="DrDoS_NetBIOS"):
    if ty == "DrDoS_NetBIOS":
        length = 14
    elif ty == "BENIGN":
        length = 14
    else:
        length = 0
    length = length + 1
    duration = nump.zeros(length)
    timestamps = []

    vin = nump.zeros(length)
    vout = nump.zeros(length)

    with open('../../data/CSV-01-12/01-12/DrDoS_NetBIOS.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        c = 0   # c counts for each edge
        i = 0   # i counts for each timestamp
        clients = []
        servers = []

        current_timestamp = 0
        for row in reader:
            elements_1 = row[0].split(",")
            elements_2 = row[1].split(",")
            type = elements_2[len(elements_2) - 1]
            previous_timestamp = current_timestamp
            if 0 <= c:
                if c > 0:
                    client_ip = elements_1[2]
                    server_ip = elements_1[4]
                    if type == ty:
                        if not(client_ip in clients):
                            clients.append(client_ip)
                        if not(server_ip in servers):
                            servers.append(server_ip)
                        timestamp = elements_2[0].split(":")[1]
                        current_timestamp = timestamp
                        flow_duration = elements_2[1]
                        duration[i] = int(flow_duration) // 60000000 + 1
                        if current_timestamp != previous_timestamp:
                            previous_timestamp = current_timestamp

                            timestamps.append(timestamp)
                            clients = []
                            servers = []
                            i = i + 1
                        else:
                            current = nump.count_nonzero(duration)
                            vin[i] = current + len(clients)
                            vout[i] = current + len(servers)
                        duration[duration > 0] -= 1
            else:
                break

            c = c + 1

    print(c)
    print(i)
    return vin, vout


drdos_netbios_ana()
drdos_netbios_ana("BENIGN")
