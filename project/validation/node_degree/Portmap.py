import numpy as nump
import csv
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plot


def vali():
    length = 929
    length += 1
    duration = nump.zeros(length)
    node_degree = nump.zeros(length)
    client_degree = nump.zeros(length)
    server_degree = nump.zeros(length)
    timestamps = []
    c = 0  # c counts for each edge
    i = 0  # i counts for each timestamp

    predictions = nump.zeros(length)
    labels = nump.zeros(length)
    with open('../../../data/CSV-03-11/03-11/Portmap.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        clients = []
        servers = []
        current_edge_client = 0
        current_edge_server = 0
        current_edge_total = 0
        current_timestamp = 0
        for row in reader:
            elements_1 = row[0].split(",")
            elements_2 = row[1].split(",")
            type = elements_2[len(elements_2) - 1]
            if type == "BENIGN":
                labels[i] = 0
            else:
                labels[i] = 1
            previous_timestamp = current_timestamp
            if 0 <= c:
                if c > 0:
                    client_ip = elements_1[2]
                    server_ip = elements_1[4]
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
                        if node_degree[i] <= 46 + 97:
                            predictions[i] = 0
                        else:
                            predictions[i] = 1
                        timestamps.append(timestamp)
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
    print(i)
    print(c)
    return labels, predictions


l, p = vali()
con = confusion_matrix(l, p)
print(classification_report(l, p))
