import numpy as nump
import csv
import matplotlib.pyplot as plot


def drdos_ssdp_ana(ty="DrDoS_SSDP"):
    if ty == "DrDoS_SSDP":
        length = 823
    elif ty == "BENIGN":
        length = 166
    else:
        length = 0
    # length = 166  # DrDoS_SSDP, 823 for attack, 166 for benign
    length = length + 1
    duration = nump.zeros(length)
    node_degree = nump.zeros(length)
    client_degree = nump.zeros(length)
    server_degree = nump.zeros(length)
    timestamps = []
    benigns = []
    with open('../../data/CSV-01-12/01-12/DrDoS_SSDP.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        c = 0   # c counts for each edge
        i = 0   # i counts for each timestamp
        nodes = []   # each ip is regarded as a node
        clients = []
        servers = []
        current_edge_client = 0
        current_edge_server = 0
        current_edge_total = 0
        # graph metrics
        # static metrics
        average_vin = 0
        average_vout = 0
        average_vino = 0
        kmax = 0
        edd = 0
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
                        timestamp = elements_2[0].split(".")[0]
                        current_timestamp = timestamp
                        flow_duration = elements_2[1]
                        duration[i] = int(flow_duration) // 1000000 + 1
                        if current_timestamp != previous_timestamp:
                            previous_timestamp = current_timestamp

                            client_degree[i] = current_edge_client

                            server_degree[i] = current_edge_server
                            node_degree[i] = current_edge_total

                            timestamps.append(timestamp)
                            average_vin = 0
                            average_vout = 0
                            average_vino = 0
                            kmax = 0
                            edd = 0
                            i = i + 1
                            current_edge_client = 0
                            current_edge_server = 0
                            current_edge_total = 0
                        else:
                            current = nump.count_nonzero(duration)
                            current_edge_client += current
                            current_edge_server += current
                            current_edge_total += 2 * current
                        duration[duration > 0] -= 1
            else:
                break

            c = c + 1

    # print("Node degree averaged over time by second:")
    # print(nump.average(node_degree))
    # print("Variance of node degree:")
    # print(nump.var(node_degree))
    # print("Standard deviation of node degree:")
    # print(nump.std(node_degree))
    # print(nump.average(client_degree))
    # print(nump.average(server_degree))
    # plot.plot(range(100), node_degree[0:100])
    # plot.show()
    # plot.plot(range(100, 200), node_degree[200:300])
    # plot.show()
    # plot.plot(range(300, 400), node_degree[300:400])
    # plot.show()
    # print(i)
    # print(c)
    return node_degree


drdos_ssdp_ana()
