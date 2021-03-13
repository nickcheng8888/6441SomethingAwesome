#! /usr/bin/env python
from scapy.all import *
conf.use_pcap = True

a=sniff(count = 1, prn=lambda x: x.show())
a.nsummary()