from networkx.algorithms import isomorphism
import networkx as nx
import numpy as nump
import csv
import matplotlib.pyplot as plot


def syn_vf2(begin, end):
    isos = 0
    nonisos = 0
    with open('../../../data/CSV-01-12/01-12/Syn.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        c = 0   # c counts for each edge
        syn_graph = nx.MultiDiGraph()
        pre_syn_graph = nx.MultiDiGraph()
        for row in reader:
            elements_1 = row[0].split(",")
            if 0 <= c:
                if begin <= c < end:
                    client_ip = elements_1[2]
                    server_ip = elements_1[4]
                    client_port = elements_1[3]
                    server_port = elements_1[5]
                    syn_graph.add_node(client_ip)
                    syn_graph.add_node(server_ip)
                    syn_graph.add_edge(client_ip + client_port, server_ip + server_port)
            else:
                break
            c = c + 1

    # colors = []
    # for n in syn_graph:
    #     if str(n).split(".")[0] == "172":
    #         colors.append('red')
    #     else:
    #         colors.append('yellow')
    # fig = plot.figure()
    # nx.draw(syn_graph, node_color=colors, node_size=10, edge_color='b')
    # fig.set_facecolor("#00000F")
    # plot.show()
    return syn_graph


# g1 = syn_vf2(begin=1000, end=1021)
# g2 = syn_vf2(begin=2000, end=2021)
# M = isomorphism.MultiDiGraphMatcher(g1, g2)
# print(M.is_isomorphic())
# syn_vf2(begin=200, end=1000)
