"""
This Module computes the triangle index of a signed directed graph.
"""

import copy
	
###############################################################################
def gen_neighbors(graph,i):
	for j in range(len(graph[i])):
		if graph[i][j]!=0:
			yield j

###############################################################################
def gen_cyclic_permutation(inp_list):
	n = len(inp_list)
	last_idx = len(inp_list) - 1
	old_list = copy.deepcopy(inp_list)

	for __ in range(n):
		new_list = [old_list[last_idx]] + old_list[:-1]
		yield new_list
		old_list = copy.deepcopy(new_list) 
		
		
###############################################################################

def is_seen_cycle(triads, inp_triad):
	for triad in triads:
		if list(inp_triad) in gen_cyclic_permutation(list(triad)):
			return True
	return False

###############################################################################
"""
Method to calculate the triangle index
"""

def calc_triangle_idx(graph,n):
	num_frustrated_triads = 0
	triads = set()
	#print(graph)

	for i in range(n):
		for j in gen_neighbors(graph,i):
			for k in gen_neighbors(graph,j):
				#print [i,j,k]
				
				is_frustrated_cyclic_triad = False
				is_frustrated_acyclic_triad = False
				
				cyclic_triad_val = graph[i][j]*graph[j][k]*graph[k][i]
				acyclic_triad_val = graph[i][j]*graph[j][k]*graph[i][k]
				
				if cyclic_triad_val == 0 and acyclic_triad_val == 0:
					continue
						
				if cyclic_triad_val == -1:
					is_frustrated_cyclic_triad = True
				if acyclic_triad_val == -1:
					is_frustrated_acyclic_triad = True
				
				is_seen_cycle_var = is_seen_cycle(triads, ((i,j),(j,k),(k,i)))
				#print is_seen_cycle_var
			
				num_frustrated_triads += int(is_frustrated_acyclic_triad)
				if not is_seen_cycle_var:
					num_frustrated_triads += int(is_frustrated_cyclic_triad)
			
				if cyclic_triad_val != 0 and acyclic_triad_val != 0:
					if not is_seen_cycle_var:
						triads.add(((i,j),(j,k),(k,i)))
					triads.add(((i,j),(j,k),(i,k)))
				elif cyclic_triad_val != 0 and not is_seen_cycle_var:
					triads.add(((i,j),(j,k),(k,i)))
				elif acyclic_triad_val != 0:
					triads.add(((i,j),(j,k),(i,k)))
				
	print num_frustrated_triads
	num_triads = len(triads)
	print num_triads				
	if num_triads != 0:				
		triangle_idx = float(num_frustrated_triads)/float(num_triads)	
		return triangle_idx
	else:
		return num_triads

###############################################################################	
if __name__ == "__main__":
	
	"""
	Taking in input from the user and creating the adjacency matrix.
	The first line of the input contains number of vertices.
	The following lines give the adjacency matrix.
	1: positive edge
	2: negative edge
	0: no edge
	"""	
	n = input()
	graph = []
	for __ in range(n):
		neighbors = []
		for __ in range(n):
			edge_type = input()
			if edge_type == 1:
				neighbors.append(1)
			elif edge_type == 2:
				neighbors.append(-1)
			else:
				neighbors.append(0)
		graph.append(neighbors)

	print(calc_triangle_idx(graph,n))
	print(graph)
	
				
