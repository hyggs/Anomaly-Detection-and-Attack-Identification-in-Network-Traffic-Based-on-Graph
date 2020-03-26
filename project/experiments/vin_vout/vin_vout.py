import project.experiments.vin_vout.Syn as Syn
import project.experiments.vin_vout.UDPLag as UDPLag
import project.experiments.vin_vout.DrDoS_UDP as DrDoS_UDP
import project.experiments.vin_vout.DrDoS_SSDP as DrDoS_SSDP
import project.experiments.vin_vout.DrDoS_SNMP as DrDoS_SNMP
import project.experiments.vin_vout.DrDoS_NTP as DrDoS_NTP
import project.experiments.vin_vout.DrDoS_NetBIOS as DrDoS_NetBIOS
import project.experiments.vin_vout.DrDoS_MSSQL as DrDoS_MSSQL
import project.experiments.vin_vout.DrDoS_LDAP as DrDoS_LDAP
import project.experiments.vin_vout.TFTP as TFTP
import project.experiments.vin_vout.DrDoS_DNS as DrDoS_DNS
import matplotlib.pyplot as plot


def nd_ana():
    syn_vin_a, syn_vout_a = Syn.syn_ana("Syn")
    syn_vin_b, syn_vout_b = Syn.syn_ana("BENIGN")

    udp_lag_vin_a, udp_lag_vout_a = UDPLag.udp_lag_ana("UDP-lag")
    udp_lag_vin_b, udp_lag_vout_b = UDPLag.udp_lag_ana("BENIGN")

    drdos_udp_vin_a, drdos_udp_vout_a = DrDoS_UDP.drdos_udp_ana("DrDoS_UDP")
    drdos_udp_vin_b, drdos_udp_vout_b = DrDoS_UDP.drdos_udp_ana("BENIGN")

    drdos_ssdp_vin_a, drdos_ssdp_vout_a = DrDoS_SSDP.drdos_ssdp_ana("DrDoS_SSDP")

    drdos_snmp_vin_a, drdos_snmp_vout_a = DrDoS_SNMP.drdos_snmp_ana("DrDoS_SNMP")

    drdos_ntp_vin_a, drdos_ntp_vout_a = DrDoS_NTP.drdos_ntp_ana()

    drdos_netbios_vin_a, drdos_netbios_vout_a = DrDoS_NetBIOS.drdos_netbios_ana()

    drdos_mssql_vin_a, drdos_mssql_vout_a = DrDoS_MSSQL.drdos_mssql_ana()

    drdos_ldap_vin_a, drdos_ldap_vout_a = DrDoS_LDAP.drdos_ldap_ana()

    drdos_dns_vin_a, drdos_dns_vout_a = DrDoS_DNS.drdos_dns_ana()

    tftp_vin_a, tftp_vout_a = TFTP.drdos_tftp_ana()

    plot.scatter(syn_vin_b[syn_vin_b > 0], syn_vout_b[syn_vout_b > 0], color='k', marker='o')
    plot.scatter(udp_lag_vin_b[udp_lag_vin_b > 0], udp_lag_vout_b[udp_lag_vout_b > 0], color='k', marker='o')
    plot.scatter(drdos_udp_vin_b[drdos_udp_vin_b > 0], drdos_udp_vout_b[drdos_udp_vout_b > 0], color='k', marker='o')

    plot.scatter(syn_vin_a[syn_vin_a > 0], syn_vout_a[syn_vout_a > 0], color='r', marker='v')
    plot.scatter(udp_lag_vin_a[udp_lag_vin_a > 0], udp_lag_vout_a[udp_lag_vout_a > 0], color='r', marker='v')
    plot.scatter(drdos_udp_vin_a[drdos_udp_vin_a > 0], drdos_udp_vout_a[drdos_udp_vout_a > 0], color='r', marker='v')
    plot.scatter(drdos_ssdp_vin_a[drdos_ssdp_vin_a > 0], drdos_ssdp_vout_a[drdos_ssdp_vout_a > 0], color='r', marker='v')
    plot.scatter(drdos_snmp_vin_a[drdos_snmp_vin_a > 0], drdos_snmp_vout_a[drdos_snmp_vout_a > 0], color='r', marker='v')
    plot.scatter(drdos_dns_vin_a[drdos_dns_vin_a > 0], drdos_dns_vout_a[drdos_dns_vout_a > 0], color='r', marker='v')
    plot.scatter(drdos_ldap_vin_a[drdos_ldap_vin_a > 0], drdos_ldap_vout_a[drdos_ldap_vout_a > 0], color='r', marker='v')
    plot.scatter(drdos_ntp_vin_a[drdos_ntp_vin_a > 0], drdos_ntp_vout_a[drdos_ntp_vout_a > 0], color='r', marker='v')
    plot.scatter(drdos_netbios_vin_a[drdos_netbios_vin_a > 0], drdos_netbios_vout_a[drdos_netbios_vout_a > 0], color='r', marker='v')
    plot.scatter(drdos_mssql_vin_a[drdos_mssql_vin_a > 0], drdos_mssql_vout_a[drdos_mssql_vout_a > 0], color='r', marker='v')
    plot.scatter(tftp_vin_a[tftp_vin_a > 0], tftp_vout_a[tftp_vout_a > 0], color='r', marker='v')

    plot.show()


nd_ana()
