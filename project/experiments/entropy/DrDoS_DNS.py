import numpy as nump
import project.experiments.node_degree.DrDoS_DNS as nd_drdos_dns
from scipy.stats import entropy


def ent(ty):
    node_degree_drdos_dns = nd_drdos_dns.drdos_dns(ty)
    prob_drdos_dns = nump.zeros(int(nump.max(node_degree_drdos_dns)))
    total = nump.sum(node_degree_drdos_dns)
    for i in range(len(prob_drdos_dns)):
        for j in range(len(node_degree_drdos_dns)):
            if i == node_degree_drdos_dns[j]:
                prob_drdos_dns[i] += 1
    prob_drdos_dns = prob_drdos_dns / total
    ent = entropy(prob_drdos_dns)
    return ent


print(ent("DrDoS_DNS"))
print(ent("BENIGN"))
