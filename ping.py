# A simple pinging program

import sys
import os

hostname = sys.argv[1]

if(sys.platform == 'linux2'):
    if(os.system("ping -c 1 "+hostname) == 0):
       print "[+]Ping successful to "+hostname
    else:
       print "[-]Ping unsuccessful to "+hostname

if(sys.platform == 'win32'):
    windata = os.popen("ping -n 1 "+hostname).read()
    if (windata.find('unreachable') == -1 \
        and windata[(windata.find('Received = ')+len('Recieved = '))] == '1'):
        print "[+]Ping successful to "+hostname
    else:
        print "[-]Ping unsuccessful to "+hostname
