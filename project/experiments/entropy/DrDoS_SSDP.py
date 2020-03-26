import numpy as nump
import project.experiments.node_degree.DrDoS_SSDP as nd_drdos_ssdp
from scipy.stats import entropy


def ent(ty):
    node_degree_drdos_ssdp = nd_drdos_ssdp.drdos_ssdp_ana(ty)
    prob_drdos_ssdp = nump.zeros(int(nump.max(node_degree_drdos_ssdp)))
    total = nump.sum(node_degree_drdos_ssdp)
    for i in range(len(prob_drdos_ssdp)):
        for j in range(len(node_degree_drdos_ssdp)):
            if i == node_degree_drdos_ssdp[j]:
                prob_drdos_ssdp[i] += 1
    prob_drdos_ssdp = prob_drdos_ssdp / total
    ent = entropy(prob_drdos_ssdp)
    return ent


print(ent("DrDoS_SSDP"))
print(ent("BENIGN"))
