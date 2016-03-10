# portscanner.py scans the ports of the given list or range of IPs/domains and
# ports.

import sys
import os
from socket import *
from threading import *
screenLock = Semaphore(value=1)
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('Data\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print '[+]'+str(tgtPort)+'/tcp open on '+tgtHost+" ("+str(gethostbyaddr(tgtHost)[0])+")"
        print '[+] ' + str(results)
    except:
        screenLock.acquire()
        print '[-]'+str(tgtPort)+'/tcp closed on '+tgtHost
        #+" ("+str(gethostbyaddr(tgtHost)[0])+")"
    finally:
        screenLock.release()
        connSkt.close()
def portScan(tgtHosts, tgtPorts):
    for tgtHost in tgtHosts:
        if(sys.platform == 'linux2'):
            if(os.system("ping -c 1 "+tgtHost) == 0):
                print "[+]Ping successful to "+tgtHost
            else:
               print "[-]Ping unsuccessful to "+tgtHost
               continue
        if(sys.platform == 'win32'):
            windata = os.popen("ping -n 1 "+tgtHost).read()
            if (windata.find('unreachable') == -1 \
            and windata[(windata.find('Received = ')+len('Recieved = '))] == '1'):
                print "[+]Ping successful to "+tgtHost
            else:
               print "[-]Ping unsuccessful to "+tgtHost
               continue
        for tgtPort in tgtPorts:
            t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
            t.start()
def main():
    if(len(sys.argv) == 1 or sys.argv[1] == '-h' or sys.argv[1] == '/?'):
        print "Usage: "+sys.argv[0] +" <target host[s]> <target port[s]>\n"
        print "Separate targets with commas, specify range with -. No spaces.\n"
        print "Ex: "+sys.argv[0] +" localhost 22\n"
        print sys.argv[0] +" localhost,pi.com 22,23\n"
        print sys.argv[0] +" 192.168.0.1-192.168.0.254 22-26\n"
        exit(0)
    if(sys.argv[1].find(',')!=-1):
        tgtHosts = sys.argv[1].split(',')
    elif(sys.argv[1].find('-')!=-1):
        tgtHosts = []
        IPs = sys.argv[1].split('-')
        IPone = IPs[0].split('.')
        IPtwo = IPs[1].split('.')
        for octone in range(int(IPone[0]), int(IPtwo[0])+1):
            for octtwo in range(int(IPone[1]), int(IPtwo[1])+1):
                for octthree in range(int(IPone[2]), int(IPtwo[2])+1):
                    for octfour in range(int(IPone[3]), int(IPtwo[3])+1):
                        tgtHosts.append(str(octone)+'.'+str(octtwo)+'.'+str(octthree)+'.'+str(octfour))               
    else:
        tgtHosts = [sys.argv[1]]
    if(sys.argv[2].find(',')!=-1):   
        tgtPorts = sys.argv[2].split(',')
    elif(sys.argv[2].find('-')!=-1):
        ports = sys.argv[2].split('-')
        tgtPorts = range(int(ports[0]), int(ports[1]))
    else:
        tgtPorts = [sys.argv[2]]
    portScan(tgtHosts, tgtPorts)
if __name__ == "__main__":
    main()
