#!usr/bin/env python

import scapy.all as scapy

DEST_MAC = "ff:ff:ff:ff:ff:ff"

def scan(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst=DEST_MAC)
    packet = broadcast/arp_req
    print(packet.summary())
    packet.show()

scan("10.0.2.1/24")

