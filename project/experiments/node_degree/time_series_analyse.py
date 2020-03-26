from graphviz import Digraph
import numpy as nump
import csv
import matplotlib.pyplot as plot


def graph():
    # dot = Digraph(comment='graph')
    dot = Digraph(engine='circo')

    # with open('../data/CSV-01-12/01-12/UDPLag.csv', newline='') as csvfile:
    with open('../data/CSV-01-12/01-12/Syn.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        c = 0
        for row in reader:
            elements = row[0].split(',')
            if 0 <= c:
                if c > 0:
                    elements[1] = elements[1].split('-')
                    source_IP = elements[1][0]
                    destination_IP = elements[1][1]
                    source_port = elements[1][2]
                    destination_port = elements[1][3]
                    # print(source_IP)
                    # print(destination_IP)
                    # print(source_port)
                    # print(destination_port)
                    dot.node(source_port)
                    dot.node(destination_port)
                    dot.edge(source_port, destination_port)
            else:
                break
            c = c + 1

    print(dot.source)
    dot.render('test-output/graph.gv', view=True)

    # dot = Digraph(comment='The Round Table')
    # dot.node('A', 'King Arthur')
    # dot.node('B', 'Sir Bedevere the Wise')
    # dot.node('L', 'Sir Lancelot the Brave')
    # dot.edges(['AB', 'AL'])
    # dot.edge('B', 'L', constraint='false')
    # print(dot.source)
    # dot.render('test-output/round-table.gv', view=True)


average_node_degree = nump.zeros(6000)
timestamps = []


def time_series_ana():
    with open('../data/CSV-01-12/01-12/UDPLag.csv', newline='') as csvfile:
    # with open('../data/CSV-01-12/01-12/TFTP.csv', newline='') as csvfile:
    # with open('../data/CSV-01-12/01-12/Syn.csv', newline='') as csvfile:
    # with open('../data/CSV-01-12/01-12/DrDoS_UDP.csv', newline='') as csvfile:
    # with open('../data/CSV-01-12/01-12/DrDoS_SSDP.csv', newline='') as csvfile:
    # with open('../data/CSV-01-12/01-12/DrDoS_SNMP.csv', newline='') as csvfile:
    # with open('../data/CSV-01-12/01-12/DrDoS_NTP.csv', newline='') as csvfile:
    # with open('../data/CSV-01-12/01-12/DrDoS_NetBIOS.csv', newline='') as csvfile:
    # with open('../data/CSV-01-12/01-12/DrDoS_MSSQL.csv', newline='') as csvfile:
    # with open('../data/CSV-01-12/01-12/DrDoS_LDAP.csv', newline='') as csvfile:
    # with open('../data/CSV-01-12/01-12/DrDoS_DNS.csv', newline='') as csvfile:
    # with open('../data/CSV-03-11/03-11/LDAP.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        c = 0   # c counts for each edge
        i = 0   # i counts for each timestamp in millisecond
        nodes = []    # each ip is regarded as a node
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
            previous_timestamp = current_timestamp
            if 0 <= c:
                if c > 0:
                    ip = elements[2]
                    if not(ip in nodes):
                        nodes.append(ip)
                    timestamp = elements[7]
                    current_timestamp = timestamp
                    if current_timestamp != previous_timestamp:
                        previous_timestamp = current_timestamp
                        average_node_degree[i] = average_node_degree[i] / len(nodes)
                        timestamps.append(timestamp)
                        average_vin = 0
                        average_vout = 0
                        average_vino = 0
                        kmax = 0
                        edd = 0
                        i = i + 1
                        average_node_degree[i] = average_node_degree[i - 1]
                    else:
                        average_node_degree[i] += 2

            else:
                break

            c = c + 1
    with open("../../midterm/01-12-UDPLag-meta.csv", mode='w') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|')
        writer.writerow(zip(average_node_degree[0:len(timestamps)]))
    # plot.plot(timestamps, average_node_degree[0:len(timestamps)])
    # plot.show()


time_series_ana()
