from scapy.all import *

dport = 80
dst = 'google.com' 
time_to_live = 0
new = 0 #used to check if destination reached

while (True):

	time_to_live += 1
	pkt = IP(dst=dst, ttl=time_to_live) / ICMP()
	response = sr1(pkt, verbose=0, timeout=1)
	
	try:
		if (new == response.src):
			exit("Destination reached")
	except AttributeError: pass 

	try:
		new = response.src
	except AttributeError: pass

	if response is None: 		
		print("[*] There is no reply")
		continue

	else:
		print("[{}] ".format(time_to_live), response.src)




	


