#!/usr/bin/env python

import subprocess
import optparse

IFCONFIG = "ifconfig"

def clear_screen():
    subprocess.call(["clear"])

def print_config():
    subprocess.call([IFCONFIG])

def change_mac(interface, mac):
    subprocess.call([IFCONFIG, interface, "down"])
    subprocess.call([IFCONFIG, interface, "hw", "ether", mac])
    subprocess.call([IFCONFIG, interface, "up"])
    print(interface, mac)

def parse_options():
    parser = optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    (options, argument) = parser.parse_args()
    change_mac(options.interface, options.new_mac)
    

print_config()
parse_options()
clear_screen()
print_config()
