#!usr/bin/env python

# run with sudo -E python3 ... | the -E switch preserves the enviroment

import scapy.all as scapy
import argparse

DEST_MAC = "ff:ff:ff:ff:ff:ff"
IP = "IP"
MAC = "MAC"

def print_table(ip_mac_map):
    print("\tIP\t\t\tMAC Addres")
    print("------------------------------------------------")
    
    for e in ip_mac_map:
        print(f"\t{e[IP]}\t\t{e[MAC]}")

def scan(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst=DEST_MAC)
    packet = broadcast/arp_req
    ans, unans = scapy.srp(packet, timeout=1, verbose=False)
    
    result = []
    for e in ans:
        result.append({IP: e[1].psrc, MAC: e[1].hwsrc})

    return result

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range")
    options = parser.parse_args()
    return options

options = get_args()
ip_mac_map = scan(options.target)
print_table(ip_mac_map)

