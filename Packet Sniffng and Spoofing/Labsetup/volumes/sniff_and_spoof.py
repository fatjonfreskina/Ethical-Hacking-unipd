from scapy.all import * 

# host = "1.2.3.4" 		# a non-existing host on the Internet
# host = "10.9.0.99" 	# a non-existing host on the LAN
host = "8.8.8.8" 		# an existing host on the Internet

def spoof(pkt):
	if pkt[ICMP].type == 8:	#echo request
		s_pck = IP(src=pkt[IP].dst, dst=pkt[IP].src, ihl=pkt[IP].ihl) / \
		ICMP(type=0, id=pkt[ICMP].id, seq=pkt[ICMP].seq) / \
		pkt[Raw].load

		send(s_pck, verbose = 0)
		print("packet sent")
		s_pck.show()

pkt = sniff(iface='br-bf7ac2fa875a', filter = "icmp and host " + host , prn = spoof)