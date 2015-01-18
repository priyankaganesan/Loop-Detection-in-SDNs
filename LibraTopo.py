"""
	Authors:
	Priyanka Ganesan
	Sharmila Raghu

Libra example topology
To start the topology:
$sudo mn --custom path/to/file/LibraTopo.py --topo libra_topo --mac --switch ovsk --controller remote
"""

from mininet.topo import Topo

class LibraTopo( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        super(TestTopo, self).__init__()

        # Add hosts and switches
        h1 = self.addHost( 'h1' ,ip='10.0.0.1')
        h2 = self.addHost( 'h2' ,ip='10.0.0.2')
        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )

        # Add links
        self.addLink('h1', 's1', port1 = 1, port2 = 1)
        self.addLink('s1', 's3', port1 = 2, port2 = 1)
        self.addLink('s1', 's4', port1 = 3, port2 = 1)
        self.addLink('h2', 's2', port1 = 1, port2 = 1)
        self.addLink('s2', 's3', port1 = 2, port2 = 2)
        self.addLink('s2', 's4', port1 = 3, port2 = 2)



topos = { 'libra_topo': ( lambda: LibraTopo() ) }
