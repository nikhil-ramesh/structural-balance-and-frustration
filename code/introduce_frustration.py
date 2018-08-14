"""
This code systematically introduces frustration.
"""
from triangle_idx import calc_triangle_idx
from random import sample
###############################################################################
def make_sb_sample_set(n):
	sb_sample_set = set()
	for i in range(n/2):
		for j in range(n/2):
			if i != j:
				sb_sample_set.add((i,j))
	for i in range(n/2,n):
		for j in range(n/2,n):
			if i !=j:
				sb_sample_set.add((i,j))
	
	return sb_sample_set
			
###############################################################################
def make_f_sample_set(n):
	f_sample_set = set()
	for i in range(n/2):
		for j in range(n/2,n):
			f_sample_set.add((i,j))
	for i in range(n/2,n):
		for j in range(n/2):
			f_sample_set.add((i,j))

	return f_sample_set
	
###############################################################################
def make_frustrated(graph,n,frustration_limit):
	curr_triangle_idx = calc_triangle_idx(graph,n)
	sb_sample_set = make_sb_sample_set(n)
	f_sample_set = make_f_sample_set(n)
	
	while curr_triangle_idx < frustration_limit:
		(i,j) = sample(sb_sample_set,1)[0]
		(k,l) = sample(f_sample_set,1)[0]
		
		graph[i][j],graph[k][l] = graph[k][l],graph[i][j]
		
		#sb_sample_set.remove((i,j))
		#f_sample_set.remove((k,l))
		print sb_sample_set
		print f_sample_set
		
		curr_triangle_idx = calc_triangle_idx(graph,n)
	return curr_triangle_idx	

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

	expected_frustration = 0.1
	triangle_idx = make_frustrated(graph,n,expected_frustration)
	print(graph)
	print(triangle_idx)
