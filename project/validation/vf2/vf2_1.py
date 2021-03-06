from networkx.algorithms import isomorphism
import networkx as nx
import numpy as nump
import csv
import matplotlib.pyplot as plot
import project.experiments.vf2.Syn as Syn
import project.experiments.vf2.UDPLag as UDPLag
import project.experiments.vf2.LDAP as LDAP
import project.experiments.vf2.MSSQL as MSSQL
import project.experiments.vf2.NetBIOS as NetBIOS

begins = [1, 11, 21, 31, 41, 101, 121, 131, 141, 201, 211, 221, 231, 241, 1001, 1011, 1021, 1031, 1041]
durations = [4, 9, 14]
for b in begins:
    for d in durations:

        g_syn = Syn.syn_vf2(b, b + d)
        g_udp_lag = UDPLag.udp_lag_vf2(b, b + d)
        g_ldap = LDAP.ldap_vf2(b, b + d)
        g_mssql = MSSQL.mssql_vf2(b, b + d)
        g_netbios = NetBIOS.netbios_vf2(b, b + d)
        # print(len(nx.nodes(g_syn)))
        # print(len(nx.nodes(g_mssql)))
        # print(len(nx.nodes(g_udp_lag)))
        # print(len(nx.nodes(g_ldap)))
        # print(len(nx.nodes(g_netbios)))

        samples = [g_syn, g_mssql, g_ldap, g_udp_lag, g_netbios]
        classification = nump.zeros(5)

        with open('../../../data/CSV-03-11/03-11/NetBIOS.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            c = 0  # c counts for each edge
            un_graph = nx.MultiDiGraph()
            for row in reader:
                elements_1 = row[0].split(",")
                elements_2 = row[1].split(",")
                type = elements_2[len(elements_2) - 1]
                if 0 <= c:
                    if c > 0:
                        if c % (d + 1) != 0:
                            client_ip = elements_1[2]
                            server_ip = elements_1[4]
                            client_port = elements_1[3]
                            server_port = elements_1[5]
                            un_graph.add_node(client_ip)
                            un_graph.add_node(server_ip)
                            un_graph.add_edge(client_ip + client_port, server_ip + server_port)
                        else:
                            for s in samples:
                                m = isomorphism.MultiDiGraphMatcher(s, un_graph)
                                if m.is_isomorphic():
                                    # print(str(m))
                                    classification[samples.index(s)] += 1
                            un_graph = nx.MultiDiGraph()

                c = c + 1
            print(c)
            print(classification)

