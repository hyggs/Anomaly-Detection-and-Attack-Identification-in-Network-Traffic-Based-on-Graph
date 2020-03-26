import numpy as nump
import csv
import matplotlib.pyplot as plot


def udplag_ana(ty="UDP-lag"):
    if ty == "UDP-lag":
        length = 1099
    elif ty == "BENIGN":
        length = 430
    else:
        length = 0
    # length = 1099  # UDP-Lag, 1099 for attack, 430 for benign
    length = length + 1
    duration = nump.zeros(length)
    number_of_clients = 117
    number_of_servers = 138
    total_number_of_nodes = number_of_clients + number_of_servers
    node_degree = nump.zeros(length)
    client_degree = nump.zeros(length)
    server_degree = nump.zeros(length)
    timestamps = []
    benigns = []
    with open('../../data/CSV-01-12/01-12/UDPLag.csv', newline='') as csvfile:
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

                        timestamp = elements[7].split(".")[0]   # second-by-second
                        current_timestamp = timestamp
                        flow_duration = elements[8]
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
                    # if type == "BENIGN":
                    #     benigns.append(timestamp)
            else:
                break

            c = c + 1
            # if c == 100000:
            #     print(i)
            #     plot.plot(timestamps, node_degree[0:i])
            #     plot.show()
    # print("Node degree averaged over time by second:")
    # print(nump.mean(node_degree))
    # print("Variance of node degree:")
    # print(nump.var(node_degree))
    # print("Standard deviation of node degree:")
    # print(nump.std(node_degree))
    # print(nump.average(client_degree))
    # print(nump.average(server_degree))
    # plot.plot(range(100), node_degree[0:100])
    # plot.show()
    # print(i)
    # print(c)
    # print(benigns)
    # plot.hist(node_degree)
    # plot.show()
    return node_degree


udplag_ana()
