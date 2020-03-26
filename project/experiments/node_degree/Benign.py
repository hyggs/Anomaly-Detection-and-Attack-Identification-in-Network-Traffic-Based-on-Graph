import numpy as nump
import csv
import matplotlib.pyplot as plot

length = 1000   # benign
length = length + 1
duration = nump.zeros(length)
node_degree = nump.zeros(length)
client_degree = nump.zeros(length)
server_degree = nump.zeros(length)
timestamps = []


def benign_ana():
    datasets = ['../data/CSV-01-12/01-12/UDPLag.csv',
                '../data/CSV-01-12/01-12/TFTP.csv',
                '../data/CSV-01-12/01-12/Syn.csv',
                '../data/CSV-01-12/01-12/DrDoS_UDP.csv',
                '../data/CSV-01-12/01-12/DrDoS_SSDP.csv',
                '../data/CSV-01-12/01-12/DrDoS_SNMP.csv',
                '../data/CSV-01-12/01-12/DrDoS_NTP.csv',
                '../data/CSV-01-12/01-12/DrDoS_NetBIOS.csv',
                '../data/CSV-01-12/01-12/DrDoS_MSSQL.csv',
                '../data/CSV-01-12/01-12/DrDoS_LDAP.csv',
                '../data/CSV-01-12/01-12/DrDoS_DNS.csv']
    for dataset in datasets:
        with open(dataset, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            print(dataset)
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
                        if type == "benign":
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
                else:
                    break

                c = c + 1

        print(nump.average(node_degree))
        print(nump.var(node_degree))
        print(nump.average(client_degree))
        print(nump.average(server_degree))


benign_ana()
