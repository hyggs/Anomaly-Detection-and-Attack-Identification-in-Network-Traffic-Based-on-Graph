from networkx.algorithms import isomorphism
import networkx as nx
import numpy as nump
import csv
import matplotlib.pyplot as plot
import project.experiments.vf2.Syn as Syn
import project.experiments.vf2.UDPLag as UDPLag
import project.experiments.vf2.LDAP as LDAP
import project.experiments.vf2.MSSQL as MSSQL
import project.experiments.vf2.NetBIOS as NetBIOS

g_syn = Syn.syn_vf2(1000, 1010)
g_udp_lag = UDPLag.udp_lag_vf2(1000, 1010)
g_ldap = LDAP.ldap_vf2(1000, 1010)
g_mssql = MSSQL.mssql_vf2(1500, 1510)
g_netbios = NetBIOS.netbios_vf2(1500, 1510)

# M_syn_udp_lag = isomorphism.DiGraphMatcher(g_syn, g_udp_lag)
# print(M_syn_udp_lag.is_isomorphic())
# M_syn_ldap = isomorphism.DiGraphMatcher(g_syn, g_ldap)
# print(M_syn_ldap.is_isomorphic())
M_syn_mssql = isomorphism.DiGraphMatcher(g_syn, g_mssql)
print(M_syn_mssql.is_isomorphic())
