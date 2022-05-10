from scapy.all import * 

def print_pkt(pkt):
	pkt.show()

pkt = sniff(iface='br-bf7ac2fa875a', filter='icmp', prn=print_pkt)