from graphviz import Digraph
import numpy as nump
import csv


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


def meta_ana():
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
        c = 0
        total = 0
        attacks = 0
        benign = 0
        # source = []
        # destination = []
        source_ip_port = []
        dest_ip_port = []
        for row in reader:
            # elements = row[1].split(",")
            elements = row[0].split(",")
            if 0 <= c:
                if c > 0:
                    ips = elements[1].split("-")
                    source_ip = ips[0]
                    source_port = ips[3]
                    destination_ip = ips[1]
                    destination_port = ips[2]
                    source_ip_port.append(str(source_ip) + str(source_port))
                    dest_ip_port.append(str(destination_ip) + str(destination_port))
                    # source.append(source_ip)
                    # destination.append(destination_ip)
                    # print(source_ip)
                    # print(destination_ip)
                    # type = elements[len(elements)-1]
                    # flow_duration = float(elements[1])
                    # print(flow_duration)
                    # if type == 'TFTP':
                    # if type == 'Syn':
                    # if type == 'DrDoS_UDP':
                    # if type == 'DrDoS_SSDP':
                    # if type == 'DrDoS_SNMP':
                    # if type == 'DrDoS_MSSQL':
                    # if type == 'DrDoS_LDAP':
                    # if type == 'DrDoS_DNS':
                        # attacks += 1
                    # else:
                        # benign += 1
                    # total += flow_duration
                # if c == 1:
                #     print(c)
                #     print(elements)  # print the first row
            else:
                break
            c = c + 1
    # print(c)
    # print(elements)     # print the last row
    # average_total_flow_duration = total / c
    # print("attacks: " + str(attacks))
    # print("average flow duration: " + str(average_total_flow_duration))
    # source = list(set(source))
    # destination = list(set(destination))
    # print(source)
    # print("The number of distinct source ip is " + str(len(source)))
    # print(destination)
    # print("The number of distinct destination ip is " + str(len(destination)))
    # print(len(list(set(source_ip_port))))  # count of distinct sender ip, port number pair as number of nodes
    print(len(list(set(dest_ip_port)))) # count of distinct server ip, port number pair as number of nodes


meta_ana()
