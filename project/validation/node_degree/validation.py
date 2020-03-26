import project.validation.node_degree.Syn as Syn
# import project.validation.node_degree.UDPLag as UDPLag
import project.validation.node_degree.UDP as UDP
# import project.validation.node_degree.LDAP as LDAP
# import project.validation.node_degree.MSSQL as MSSQL
# import project.validation.node_degree.Portmap as Portmap
from sklearn.metrics import classification_report

labels0, predictions0 = Syn.vali()
print(labels0)
print(type(labels0))
labels1, predictions1 = UDP.vali()
print(classification_report([labels0, labels1], [predictions0, predictions1]))


