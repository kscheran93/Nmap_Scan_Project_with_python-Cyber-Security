#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()
print('Welcome, this is a simple nmap automation tool')
print('<------------------------------------------------->')

ip_addr = input('Please enter the IP address you want to scan: ')
print('The IP you entered is:', ip_addr)

response = input("""\nPlease enter the type of scan you want to run:
                 1) SYN ACK Scan
                 2) UDP Scan
                 3) Comprehensive Scan
                 Enter option number: """)

print('You have selected option:', response)

if response == '1':
    print('Nmap Version:', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print('Scaninfo:', scanner.scaninfo())
    print('IP Status:', scanner[ip_addr].state())
    print('Open ports:', scanner[ip_addr]['tcp'].keys())
elif response == '2':
    print('Nmap Version:', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print('Scaninfo:', scanner.scaninfo())
    print('IP Status:', scanner[ip_addr].state())
    print('Open ports:', scanner[ip_addr]['udp'].keys())
elif response == '3':
    print('Nmap Version:', scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print('Scaninfo:', scanner.scaninfo())
    print('IP Status:', scanner[ip_addr].state())
    print('Open ports:', scanner[ip_addr]['tcp'].keys())
elif response >= '4':
    print('Please enter a valid option')
    
    
