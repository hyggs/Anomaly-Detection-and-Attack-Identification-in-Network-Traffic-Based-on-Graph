import project.experiments.node_degree.UDPLag as UDPLag
import project.experiments.node_degree.Syn as Syn
import project.experiments.node_degree.DrDoS_DNS as DrDoS_DNS
import project.experiments.node_degree.TFTP as TFTP
import project.experiments.node_degree.DrDoS_LDAP as DrDoS_LDAP
import project.experiments.node_degree.DrDoS_MSSQL as DrDoS_MSSQL
import project.experiments.node_degree.DrDoS_NetBIOS as DrDoS_NetBIOS
import project.experiments.node_degree.DrDoS_NTP as DrDoS_NTP
import project.experiments.node_degree.DrDoS_SNMP as DrDoS_SNMP
import project.experiments.node_degree.DrDoS_SSDP as DrDoS_SSDP
import project.experiments.node_degree.DrDoS_UDP as DrDoS_UDP
import matplotlib.pyplot as plot


def nd_ana():

    udp_lag_a = UDPLag.udplag_ana(ty="UDP-lag")
    udp_lag_b = UDPLag.udplag_ana(ty="BENIGN")
    # tftp_a = TFTP.tftp_ana(ty="TFTP")
    tftp_b = TFTP.tftp_ana(ty="BENIGN")
    syn_a = Syn.syn_ana(ty="Syn")
    syn_b = Syn.syn_ana(ty="BENIGN")
    drdos_dns_a = DrDoS_DNS.drdos_dns(ty="DrDoS_DNS")
    drdos_dns_b = DrDoS_DNS.drdos_dns(ty="BENIGN")
    drdos_ldap_a = DrDoS_LDAP.drdos_ldap(ty="DrDoS_LDAP")
    drdos_ldap_b = DrDoS_LDAP.drdos_ldap(ty="BENIGN")
    drdos_mssql_b = DrDoS_MSSQL.drdos_netbios_ana(ty="BENIGN")
    drdos_netbios_b = DrDoS_NetBIOS.drdos_netbios_ana(ty="BENIGN")
    drdos_ntp_b = DrDoS_NTP.drdos_ntp_ana(ty="BENIGN")
    drdos_snmp_b = DrDoS_SNMP.drdos_ssdp_ana(ty="BENIGN")
    drdos_ssdp_b = DrDoS_SSDP.drdos_ssdp_ana(ty="BENIGN")
    drdos_udp_b = DrDoS_UDP.drdos_udp_ana(ty="BENIGN")

    # plotting attacks
    plot.hist(udp_lag_a, bins=50, color='b')
    plot.hist(syn_a, bins=50, color='g')
    plot.hist(drdos_dns_a, bins=50, color='c')
    plot.hist(drdos_ldap_a, bins=50, color='r')

    # plotting benigns
    plot.hist(udp_lag_b, bins=50, range=(0, 1200), color='k')
    plot.hist(syn_b, bins=50, range=(0, 1200), color='k')
    plot.hist(tftp_b, bins=50, range=(0, 1200),  color='k')
    plot.hist(drdos_dns_b, bins=50, range=(0, 1200),  color='k')
    plot.hist(drdos_ldap_b, bins=50, range=(0, 1200),  color='k')
    plot.hist(drdos_mssql_b, bins=50, range=(0, 1200),  color='k')
    plot.hist(drdos_netbios_b, bins=50, range=(0, 1200),  color='k')
    plot.hist(drdos_ntp_b, bins=50, range=(0, 1200),  color='k')
    plot.hist(drdos_snmp_b, bins=50, range=(0, 1200),  color='k')
    plot.hist(drdos_ssdp_b, bins=50, range=(0, 1200),  color='k')
    plot.hist(drdos_udp_b, bins=50, range=(0, 1200),  color='k')

    # b = [udp_lag_b, tftp_b, syn_b, drdos_dns_b, drdos_ldap_b]
    # plot.hist(tftp_b, bins=50, color='k')
    # plot.legend(['UDP-Lag', 'BENIGN'])
    plot.legend(['UDP-Lag', 'Syn', 'DrDoS_DNS', 'DrDoS_LDAP', 'BENIGN'])
    plot.xlabel('total node degree')
    plot.ylabel('number of occurrence')
    plot.show()


nd_ana()
