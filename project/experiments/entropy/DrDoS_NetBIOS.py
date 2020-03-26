import numpy as nump
import project.experiments.node_degree.DrDoS_NetBIOS as nd_drdos_netbios
from scipy.stats import entropy


def ent(ty):
    node_degree_drdos_netbios = nd_drdos_netbios.drdos_netbios_ana(ty)
    prob_drdos_netbios = nump.zeros(int(nump.max(node_degree_drdos_netbios)))
    total = nump.sum(node_degree_drdos_netbios)
    for i in range(len(prob_drdos_netbios)):
        for j in range(len(node_degree_drdos_netbios)):
            if i == node_degree_drdos_netbios[j]:
                prob_drdos_netbios[i] += 1
    prob_drdos_netbios = prob_drdos_netbios / total
    ent = entropy(prob_drdos_netbios)
    return ent


print(ent("DrDoS_NetBIOS"))
print(ent("BENIGN"))
