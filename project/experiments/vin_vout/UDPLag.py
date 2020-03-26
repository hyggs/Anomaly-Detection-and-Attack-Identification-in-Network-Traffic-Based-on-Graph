import numpy as nump
import csv
import matplotlib.pyplot as plot


def udp_lag_ana(ty="UDP-lag"):
    if ty == "UDP-lag":
        length = 27
    elif ty == "BENIGN":
        length = 27
    else:
        length = 0
    length = length + 1
    duration = nump.zeros(length)
    timestamps = []

    vin = nump.zeros(length)
    vout = nump.zeros(length)

    with open('../../data/CSV-01-12/01-12/UDPLag.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        c = 0   # c counts for each edge
        i = 0   # i counts for each timestamp
        clients = []
        servers = []

        current_timestamp = 0
        for row in reader:
            elements = row[0].split(",")
            type = elements[len(elements) - 1]
            previous_timestamp = current_timestamp
            if 0 <= c:
                if c > 0:
                    client_ip = elements[2]
                    server_ip = elements[4]
                    if type == ty:
                        if not(client_ip in clients):
                            clients.append(client_ip)
                        if not(server_ip in servers):
                            servers.append(server_ip)
                        timestamp = elements[7].split(":")[0]   # minute-by-minute
                        current_timestamp = timestamp
                        flow_duration = elements[8]
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


udp_lag_ana()
udp_lag_ana("BENIGN")
