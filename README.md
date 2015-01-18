#README: Detecting Loops in SDNs: Static Data Plane Verification

---
###1. Introduction:
It aims to find loops in a test network, using static data plane verification. In this process, the networks flow table dumps are analyzed in order to create forwarding graphs. This is shown in the figure below[1].

![Forwarding graph construction](https://github.com/priyankaganesan/Loop-Detection-in-SDNs/blob/master/Process.png "Forwarding graph construction")


These graphs are partitioned based on the destination IP prefix, as seen[1].

![alt text](https://github.com/priyankaganesan/Loop-Detection-in-SDNs/blob/master/Partitioning%20based%20on%20IP.png "Partitioning based on IP")


The partitioned graphs are processed using Tarjan's algorithm for strongly connected components, in order to detect loops[1].

![alt text](https://github.com/priyankaganesan/Loop-Detection-in-SDNs/blob/master/Screen%20Shot%202014-12-10%20at%2012.00.57%20PM.png "Forwarding graphs with and without loops")


---
###2 Source
The implementation of this project is based on the paper ["Libra: Divide and Conquer to Verify Forwarding Tables in Huge Networks"](https://www.usenix.org/conference/nsdi14/technical-sessions/presentation/zeng). 

---
###3. Setup

	i. Within the VM, place the following project files in the '~pyretic/pyretic/examples' directory:
		* insertLoop.py
		* insertNoLoop.py
		* detect_loop.py
		* LibraTopo.py

	ii. In one terminal window, move to the directory '~/pyretic'. At the prompt, start the controller by typing:
		'pyretic.py -m p0 pyretic.examples.insertNoLoop'

	iii. In a second terminal window, move to '~/pyretic/pyretic/examples' and start the LibraTopo topology using the following command:
		'sudo mn --custom ~pyretic/pyretic/examples/LibraTopo.py --topo libra_topo --mac --switch ovsk --controller remote'

	iv. In a third terminal window move to '~/pyretic/pyretic/examples' and start the loop detection program:
		'python detect_loop.py'

	v. Since we have used a controller which will not input loops in the topology, we will get the following messages:
		>Testing topology for destination IP 10.0.0.1
		>No loop detected!
		>Testing topology for destination IP 10.0.0.2
		>No loop detected!

	vi. Kill the processes in the current windows. Repeat steps (ii)-(iv) using the 'insertLoop' controller. In this case, the output will be:
		>Testing topology for destination IP 10.0.0.1
		>Loop detected between the switches (4,3,1)
		>Testing topology for destination IP 10.0.0.2
		>No loop detected!

	vii. The flow dumps will be generated in the files s1.txt, s2.txt, s3.txt, s4.txt

---
###4. Demonstration Video
<a href="http://www.youtube.com/watch?feature=player_embedded&v=apSwy9G-kx4
" target="_blank"><img src="http://img.youtube.com/vi/apSwy9G-kx4/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

---
###5. Authors
1. Ganesan, Priyanka (priyanka.ganesan@gatech.edu)
2. Raghu, Sharmila (sraghu7@gatech.edu)

###6. References
1. Zeng, Hongyi. "Libra: Divide and Conquer to Verify Forwarding Tables in Huge Networks." Proceedings of the 11th USENIX Symposium on Networked Systems Design and Implementation (NSDI ’14). USA, Seattle, WA. USENIX Association, n.d. Web. <https://www.usenix.org/system/files/conference/nsdi14/nsdi14-paper-zeng.pdf>.
2. Monsanto, Christopher, Joshua Reich, Nate Foster, Jennifer Rexford, and David Walker. "Composing Software Defined Networks." 10th USENIX Symposium on Networked Systems Design and Implementation (NSDI 13). United States, Lombard, IL. USENIX Association, n.d. Web. <https://www.usenix.org/conference/nsdi13/technical-sessions/presentation/monsanto>.

