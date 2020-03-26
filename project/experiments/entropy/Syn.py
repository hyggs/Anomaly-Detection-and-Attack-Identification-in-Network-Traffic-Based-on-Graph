import numpy as nump
import project.experiments.node_degree.Syn as nd_syn
from scipy.stats import entropy


def ent(ty):
    node_degree_syn = nd_syn.syn_ana(ty)
    prob_syn = nump.zeros(int(nump.max(node_degree_syn)))
    total = nump.sum(node_degree_syn)
    for i in range(len(prob_syn)):
        for j in range(len(node_degree_syn)):
            if i == node_degree_syn[j]:
                prob_syn[i] += 1
    prob_syn = prob_syn / total
    ent = entropy(prob_syn)
    return ent


print(ent("Syn"))
print(ent("BENIGN"))
