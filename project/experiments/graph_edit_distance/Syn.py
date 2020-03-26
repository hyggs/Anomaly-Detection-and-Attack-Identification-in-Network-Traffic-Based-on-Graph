import numpy as nump
import csv
import gc
import matplotlib.pyplot as plot
from networkx.algorithms.similarity import graph_edit_distance
from networkx.algorithms.similarity import optimize_graph_edit_distance
import networkx as nx


def ged(ty="Syn"):
    if ty == "Syn":
        length = 238
    elif ty == "BENIGN":
        length = 68
    else:
        length = 0
    # length = 238 + 68  # Syn, 238 for attack, 68 for benign
    length = length + 1
    duration = nump.zeros(length)
    node_degree = nump.zeros(length)
    client_degree = nump.zeros(length)
    server_degree = nump.zeros(length)
    timestamps = []
    graph_edit_distances = nump.zeros(7)
    benign_count = 0
    with open('../../../data/CSV-01-12/01-12/Syn.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        c = 0   # c counts for each edge
        i = 0
        j = 0
        g = 0
        nodes = []   # each ip is regarded as a node
        clients = []
        servers = []
        current_edge_client = 0
        current_edge_server = 0
        current_edge_total = 0
        current_timestamp = 0
        benigns = nump.zeros(length)
        previous_graph = nx.MultiDiGraph()
        current_graph = nx.MultiDiGraph()
        for row in reader:
            elements_1 = row[0].split(",")
            elements_2 = row[1].split(",")
            type = elements_2[len(elements_2) - 1]
            previous_timestamp = current_timestamp
            if 0 <= c:
                if 1015 < c < 1023 and type == ty and ty == "Syn":
                    client_ip = elements_1[2]
                    server_ip = elements_1[4]
                    client_port = elements_1[3]
                    server_port = elements_1[5]
                    current_graph.add_node(client_ip)
                    current_graph.add_node(server_ip)
                    current_graph.add_edge(client_ip + client_port, server_ip + server_port)
                    print(i)
                    graph_edit_distances[i] = graph_edit_distance(previous_graph, current_graph)
                    previous_graph = current_graph.copy()
                    i += 1
                elif ty == "BENIGN" and type == ty and 1 < c < 2500:
                    client_ip = elements_1[2]
                    server_ip = elements_1[4]
                    client_port = elements_1[3]
                    server_port = elements_1[5]
                    current_graph.add_node(client_ip)
                    current_graph.add_node(server_ip)
                    current_graph.add_edge(client_ip + client_port, server_ip + server_port)
                    print(j)
                    g += graph_edit_distance(previous_graph, current_graph)
                    previous_graph = current_graph.copy()
                    j += 1
                    g = g / j
            else:
                break

            c = c + 1
    if ty == "BENIGN":
        graph_edit_distances = nump.repeat(g, 7)
        print(graph_edit_distances)
    print("start:")
    return graph_edit_distances


ga = ged("Syn")
plot.plot(ga, color="r")
# gb = ged("BENIGN")
# gb = nump.average(gb)
plot.plot(nump.repeat(3, 7), color="k")
plot.ylabel("graph edit distance")
plot.xlabel("time/microsecond")
plot.legend(["Syn", "benign"])
plot.show()

