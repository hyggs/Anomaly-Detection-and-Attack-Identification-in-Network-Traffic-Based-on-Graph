import numpy as nump
import project.experiments.node_degree.DrDoS_NTP as nd_drdos_ntp
from scipy.stats import entropy


def ent(ty):
    node_degree_drdos_ntp = nd_drdos_ntp.drdos_ntp_ana(ty)
    prob_drdos_ntp = nump.zeros(int(nump.max(node_degree_drdos_ntp)))
    total = nump.sum(node_degree_drdos_ntp)
    for i in range(len(prob_drdos_ntp)):
        for j in range(len(node_degree_drdos_ntp)):
            if i == node_degree_drdos_ntp[j]:
                prob_drdos_ntp[i] += 1
    prob_drdos_ntp = prob_drdos_ntp / total
    ent = entropy(prob_drdos_ntp)
    return ent


print(ent("DrDoS_NTP"))
print(ent("BENIGN"))
