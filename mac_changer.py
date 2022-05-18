#!/usr/bin/env python

import subprocess
import optparse
import re

IFCONFIG = "ifconfig"

def clear_screen():
    subprocess.call(["clear"])

def print_config():
    subprocess.call([IFCONFIG])

def change_mac(interface, mac):
    print(interface, mac)
    subprocess.call([IFCONFIG, interface, "down"])
    subprocess.call([IFCONFIG, interface, "hw", "ether", mac])
    subprocess.call([IFCONFIG, interface, "up"])
    print(interface, mac)

def parse_options():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    return parser.parse_args()
    
def check_changed_mac(interface):
    ifc_result = subprocess.check_output(["ifconfig", interface])
    mac_result = re.search(r"([a-z|0-9]{2}:){5}[a-z|0-9]{2}", ifc_result.decode("utf-8"))
    if mac_result:
        return mac_result.group(0)
    else:
        return None

def check_success(mac_input, changed_mac):
    if changed_mac and (mac_input == changed_mac):
        print(changed_mac, " --- ", "mac changed successfully")
    else:
        print("the mac was not changed")

print_config()
(options, argument) = parse_options()
change_mac(options.interface, options.new_mac)
clear_screen()
print_config()
changed_mac = check_changed_mac(options.interface)
check_success(options.new_mac, changed_mac)

