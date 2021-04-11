#! /usr/bin/env python
from scapy.all import *
conf.use_pcap = True
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
#post-5236 > div.container-fluid > div:nth-child(1) > form > div > input
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
DRIVER_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
driver = webdriver.Chrome(executable_path = DRIVER_BIN)
def print_packet(packet):
    ip_layer = packet.getlayer(IP)
    src = ip_layer.src
    if '192.168' not in src:
        driver.get('https://www.whatismyip.com/' + src + '/') 
        driver.execute_script("window.scrollTo(0, 30)") 
        try:
            driver.find_elements_by_xpath("//*[contains(text(), 'ISP:')]").click()
        except:
            print('continue')

        el = driver.find_element_by_xpath("//*[contains(text(), 'ISP:')]")
        print("[!] Host: ", end = '')
        print(el.text)
       
a=sniff(iface = "en0", filter = "ip", prn=print_packet)

