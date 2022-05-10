from scapy.all import * 

def print_pkt(pkt):
	pkt.show()

pkt = sniff(iface='br-bab1907c5b24', filter='tcp', prn=print_pkt)