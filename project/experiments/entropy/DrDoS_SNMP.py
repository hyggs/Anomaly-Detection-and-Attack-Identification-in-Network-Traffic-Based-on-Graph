import numpy as nump
import project.experiments.node_degree.DrDoS_SNMP as nd_drdos_snmp
from scipy.stats import entropy


def ent(ty):
    node_degree_drdos_snmp = nd_drdos_snmp.drdos_snmp_ana(ty)
    prob_drdos_snmp = nump.zeros(int(nump.max(node_degree_drdos_snmp)))
    total = nump.sum(node_degree_drdos_snmp)
    for i in range(len(prob_drdos_snmp)):
        for j in range(len(node_degree_drdos_snmp)):
            if i == node_degree_drdos_snmp[j]:
                prob_drdos_snmp[i] += 1
    prob_drdos_snmp = prob_drdos_snmp / total
    ent = entropy(prob_drdos_snmp)
    return ent


print(ent("DrDoS_SNMP"))
print(ent("BENIGN"))
