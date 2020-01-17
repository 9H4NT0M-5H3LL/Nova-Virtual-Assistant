#!/usr/bin/env python
from main import talk
def nmapScan(command):
    network = command[-1]
    print("[+] Scanning the network {} for open ports".format(network))
    import nmap
    nmScan = nmap.PortScanner() #Initialise the portScanner
    nmScan.scan(network)    #Scanning the network
    cmdline = nmScan.command_line()
    print(cmdline)
    for host in nmScan.all_hosts():
        hostname = nmScan[host].hostname()
        state = nmScan[host].state()
        for proto in nmScan[host].all_protocols():
        #protocol = nmScan[host].all_protocols()
            lport = nmScan[host][proto].keys()
            sts = []
            for port in lport:
                sts.append(nmScan[host][proto][port]['state'])
            talk("the host {} is {}. the ports found are {} whose status are {}.".format(hostname,state,lport,sts))

command = input("enter command: ").split(" ")
print(command)
nmapScan(command)
#talk("Which network you want to scan ?")