import numpy as nump
import project.experiments.node_degree.DrDoS_MSSQL as nd_drdos_mssql
from scipy.stats import entropy


def ent(ty):
    node_degree_drdos_mssql = nd_drdos_mssql.drdos_mssql_ana(ty)
    prob_drdos_mssql = nump.zeros(int(nump.max(node_degree_drdos_mssql)))
    total = nump.sum(node_degree_drdos_mssql)
    for i in range(len(prob_drdos_mssql)):
        for j in range(len(node_degree_drdos_mssql)):
            if i == node_degree_drdos_mssql[j]:
                prob_drdos_mssql[i] += 1
    prob_drdos_mssql = prob_drdos_mssql / total
    ent = entropy(prob_drdos_mssql)
    return ent


print(ent("DrDoS_MSSQL"))
print(ent("BENIGN"))
