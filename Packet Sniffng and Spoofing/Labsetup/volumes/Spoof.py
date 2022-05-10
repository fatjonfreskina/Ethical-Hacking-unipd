from scapy.all import *

ip = IP(src=RandIP(),dst='10.9.0.5') #Host A
icmp = ip/ICMP() 
send(icmp)




