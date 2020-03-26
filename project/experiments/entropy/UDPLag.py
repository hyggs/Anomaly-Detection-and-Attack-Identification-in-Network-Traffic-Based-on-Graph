import numpy as nump
import project.experiments.node_degree.UDPLag as nd_udp
from scipy.stats import entropy


def ent(ty):
    node_degree_udp = nd_udp.udplag_ana(ty)
    prob_udp = nump.zeros(int(nump.max(node_degree_udp)))
    total = nump.sum(node_degree_udp)
    for i in range(len(prob_udp)):
        for j in range(len(node_degree_udp)):
            if i == node_degree_udp[j]:
                prob_udp[i] += 1
    prob_udp = prob_udp / total
    ent = entropy(prob_udp)
    return ent


print(ent("UDP-lag"))
print(ent("BENIGN"))
