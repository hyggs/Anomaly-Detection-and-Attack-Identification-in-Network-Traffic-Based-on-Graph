import numpy as nump
import project.experiments.node_degree.TFTP as nd_tftp
from scipy.stats import entropy


def ent(ty):
    node_degree_tftp = nd_tftp.tftp_ana(ty)
    prob_tftp = nump.zeros(int(nump.max(node_degree_tftp)))
    total = nump.sum(node_degree_tftp)
    for i in range(len(prob_tftp)):
        for j in range(len(node_degree_tftp)):
            if i == node_degree_tftp[j]:
                prob_tftp[i] += 1
    prob_tftp = prob_tftp / total
    ent = entropy(prob_tftp)
    return ent


print(ent("TFTP"))
print(ent("BENIGN"))
