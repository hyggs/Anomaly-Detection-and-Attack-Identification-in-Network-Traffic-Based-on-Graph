import numpy as nump
import project.experiments.node_degree.DrDoS_UDP as nd_drdos_udp
from scipy.stats import entropy


def ent(ty):
    node_degree_drdos_udp = nd_drdos_udp.drdos_udp_ana(ty)
    prob_drdos_udp = nump.zeros(int(nump.max(node_degree_drdos_udp)))
    total = nump.sum(node_degree_drdos_udp)
    for i in range(len(prob_drdos_udp)):
        for j in range(len(node_degree_drdos_udp)):
            if i == node_degree_drdos_udp[j]:
                prob_drdos_udp[i] += 1
    prob_drdos_udp = prob_drdos_udp / total
    ent = entropy(prob_drdos_udp)
    return ent


print(ent("DrDoS_UDP"))
print(ent("BENIGN"))
