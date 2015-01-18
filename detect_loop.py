'''
	Authors:
	Priyanka Ganesan
	Sharmila Raghu
'''

import re
import os

def read_flows():
	graphs={'10.0.0.1':{},'10.0.0.2':{}}
	#For each switch in the topology
	for x in range(1,5):

		#Get flow dump using ovs-ofctl
		os.system('sudo ovs-ofctl dump-flows s'+str(x)+' > s'+str(x)+'.txt')
		with open('s'+str(x)+'.txt', 'r') as fp:
			file_lines=fp.readlines()
			for line in file_lines:

				#Extract lines from flow dump which have destination IP and output ports
				if (line.find("ip") is not -1) and (line.find("in_port") is -1):
					index=line.find("ip")
					sub=line[index:]

					#Extract destination IP
					ip_obj=re.search(r'[0-9]+(?:\.[0-9]+){3}',sub)
					ip=ip_obj.group()

					#Extract output ports
					outports=[]
					output_list=re.findall('output:[0-9]*',sub)
					for i in output_list:
						outport=re.search(r'\d+',i)
						outports.append(outport.group())
	
					#For particular dst_ip, create adjacency list with switch and output ports
					if(ip == '10.0.0.1'):
						graphs['10.0.0.1'][x]=outports
					elif(ip == '10.0.0.2'):
						graphs['10.0.0.2'][x]=outports
	return graphs
	
					
def strongly_connected_components(graph):

     index_counter = [0]
     stack = []
     lowlinks = {}
     index = {}
     result = []
 
     def strongconnect(node):
         # set the depth index for this node to the smallest unused index
         index[node] = index_counter[0]
         lowlinks[node] = index_counter[0]
         index_counter[0] += 1
         stack.append(node)
 
         # Consider successors of `node`
         try:
             successors = graph[node]
         except:
             successors = []
         for successor in successors:
             if successor not in lowlinks:
                 # Successor has not yet been visited; recurse on it
                 strongconnect(successor)
                 lowlinks[node] = min(lowlinks[node],lowlinks[successor])
             elif successor in stack:
                 # the successor is in the stack and hence in the current strongly connected component (SCC)
                 lowlinks[node] = min(lowlinks[node],index[successor])
 
         # If `node` is a root node, pop the stack and generate an SCC
         if lowlinks[node] == index[node]:
             connected_component = []
 
             while True:
                 successor = stack.pop()
                 connected_component.append(successor)
                 if successor == node: break
             component = tuple(connected_component)
             # storing the result
             result.append(component)
 
     for node in graph:
         if node not in lowlinks:
             strongconnect(node)
 
     return result

def main():
	#Extract information from flow dump
	g=read_flows()

	#Mapping between output ports and destination switches
	topo = {
		1:{'1':10,'2':3,'3':4},
		2:{'1':11,'2':3,'3':4},
		3:{'1':1,'2':2},
		4:{'1':1,'2':2}
	}
	
	#Modify flow information g to have destination switches instead of output ports
	for ip in g:
		for switch in range(1,5):
			for i in range(0,len(g[ip][switch])):
				g[ip][switch][i]= topo[switch][g[ip][switch][i]]

	'''Sample adjacency list which has loop
	insertLoop1 = {
		1:[3,4],
		2:[3,4],
		3:[1],
		4:[1]
	}

	Sample adjacency list with no loop
	insertLoop2={
		1:[3,4],
		2:[11],
		3:[2],
		4:[2]
	}'''

	#Check for loops depending on a flow's destination IP address
	#For a particular destination, prints either
		#(i)List of switches where loop was found
		#(ii)No loop detected
	for ip in g:
		print "\nTesting topology for destination IP ",ip
		result = strongly_connected_components(g[ip])
		flag=0
		for x in result:
			count=0
			for switch in x:
				count=count+1
			if count> 1:
				flag=1
				print "Loop detected between the switches",x 
		if flag is 0:
			print "No loop detected!"

if __name__ == '__main__':
        main()
                                                                                                                                                      
