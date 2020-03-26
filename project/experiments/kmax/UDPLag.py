import numpy as nump
import csv
import matplotlib.pyplot as plot


def udp_lag_ana():
    # if ty == "UDP-lag":
    #     length = 1099
    # elif ty == "BENIGN":
    #     length = 430
    # else:
    #     length = 0
    length = 1099
    length = length + 1
    duration = nump.zeros(length)
    timestamps = []

    kmax = nump.zeros(length)
    kmax_a = nump.zeros(length)
    kmax_b = nump.zeros(length)
    with open('../../../data/CSV-01-12/01-12/UDPLag.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        c = 0   # c counts for each edge
        i = 0   # i counts for each timestamp
        clients = []
        servers = []

        current_timestamp = 0
        o1 = 0
        o2 = 0
        for row in reader:
            elements = row[0].split(",")
            type = elements[len(elements) - 1]
            if type == "WebDDoS":
                continue
            previous_timestamp = current_timestamp
            if 0 <= c:
                if c > 0:
                    client_ip = elements[2]
                    server_ip = elements[4]
                    clients.append(client_ip)
                    o1 = o1 + 1
                    servers.append(server_ip)
                    o2 = o2 + 1

                    timestamp = elements[7].split(".")[0]
                    current_timestamp = timestamp
                    flow_duration = elements[8]
                    if flow_duration == '':
                        continue
                    duration[i] = int(flow_duration) // 1000000 + 1
                    if current_timestamp != previous_timestamp:
                        previous_timestamp = current_timestamp
                        c_uni = nump.unique(clients, return_counts=True)[1]
                        s_uni = nump.unique(servers, return_counts=True)[1]
                        c_max = nump.max(c_uni)
                        s_max = nump.max(c_uni)
                        kmax[i] = max(c_max, s_max)
                        if type == "UDP-lag":
                            kmax_a[i] = kmax[i]
                        elif type == "BENIGN":
                            kmax_b[i] = kmax[i]
                        clients = []
                        servers = []
                        o1 = 0
                        o2 = 0

                        timestamps.append(timestamp)
                        clients = []
                        servers = []
                        i = i + 1
                    else:
                        current = nump.count_nonzero(duration)
                    duration[duration > 0] -= 1
            else:
                break

            c = c + 1

    print(c)
    print(i)
    print(nump.max(kmax_b))
    print(nump.min(kmax_b))

    plot.plot(kmax_a[3:-2], 'r')
    plot.plot(kmax_b[3:-2], 'k')
    plot.xlabel("time/s")
    plot.ylabel("kmax")
    plot.show()
    return kmax


udp_lag_ana()
