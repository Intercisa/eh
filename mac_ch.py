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

    return parser.parse_args()
    

#print_config()
#(options, argument) = parse_options()
#change_mac(options.interface, options.new_mac)
clear_screen()
#print_config()

print(subprocess.check_output(["ifconfig"]))
