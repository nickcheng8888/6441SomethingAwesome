#! /usr/bin/env python
from scapy.all import *
conf.use_pcap = True
from selenium import webdriver
import os
#post-5236 > div.container-fluid > div:nth-child(1) > form > div > input
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
DRIVER_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

def print_packet(packet):
    ip_layer = packet.getlayer(IP)
    src = ip_layer.src
    driver = webdriver.Chrome(executable_path = DRIVER_BIN)
    driver.get('https://www.whatismyip.com/' + src + '/')
    print("[!] New Packet:")

    

a=sniff(iface = "en0", filter = "ip", prn=print_packet)

