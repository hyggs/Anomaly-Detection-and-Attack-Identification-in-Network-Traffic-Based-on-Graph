import numpy as nump
import project.experiments.node_degree.DrDoS_LDAP as nd_drdos_ldap
from scipy.stats import entropy


def ent(ty):
    node_degree_drdos_ldap = nd_drdos_ldap.drdos_ldap(ty)
    prob_drdos_ldap = nump.zeros(int(nump.max(node_degree_drdos_ldap)))
    total = nump.sum(node_degree_drdos_ldap)
    for i in range(len(prob_drdos_ldap)):
        for j in range(len(node_degree_drdos_ldap)):
            if i == node_degree_drdos_ldap[j]:
                prob_drdos_ldap[i] += 1
    prob_drdos_ldap = prob_drdos_ldap / total
    ent = entropy(prob_drdos_ldap)
    return ent


print(ent("DrDoS_LDAP"))
print(ent("BENIGN"))
