#!usr/bin/env python

import scapy.all as scapy

def scan(ip):
    result = scapy.ARP(ip)
    print(result)


scan("10.0.2.2")

