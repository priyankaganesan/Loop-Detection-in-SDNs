'''
	Authors:
	Priyanka Ganesan
	Sharmila Raghu
'''

from pyretic.lib.corelib import *
from pyretic.lib.std import *
from pyretic.lib.query import *

#Destination host IP addresses
ip1 = IPAddr('10.0.0.1')
ip2 = IPAddr('10.0.0.2')

#Installs flow rules with 2 loops into corresponding LibraTopo.py topology
policy=(	(((match(switch=1, dstip=ip2)) >> (fwd(2)+fwd(3)))+
			((match(switch=1,dstip=ip1))>>(fwd(2)+fwd(3))))+
			(((match(switch=2, dstip=ip1)) >> (fwd(2)+fwd(3)))+
			((match(switch=2,dstip=ip2))>>fwd(1)))+
			(((match(switch=3, dstip=ip1)) >> (fwd(1)))+
			((match(switch=3,dstip=ip2))>>fwd(2)))+
			(((match(switch=4, dstip=ip1)) >> (fwd(1)))+
			((match(switch=4,dstip=ip2))>>fwd(2)))		)

def main():
    return policy
