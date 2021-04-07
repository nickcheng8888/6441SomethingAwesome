#! /usr/bin/env python
from scapy.all import *
conf.use_pcap = True

def print_packet(packet):
    ip_layer = packet.getlayer(IP)
    print("[!] New Packet: {src} -> {dst}".format(src=ip_layer.src, dst=ip_layer.dst))

a=sniff(iface = "en0", filter = "ip", prn=print_packet)
