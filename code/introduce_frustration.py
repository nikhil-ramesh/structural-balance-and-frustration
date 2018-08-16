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
def make_frustrated_by_swapping(graph,n,frustration_limit):
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
def get_edge_list(graph,n):
	edge_list = []
	
	for i in range(n):
		for j in range(n):
			if graph[i][j]!=0:
				edge_list.append((i,j))
				
	return edge_list

###############################################################################
def gen_frustration_by_edge(graph,n,frustration_limit):
	curr_triangle_idx = calc_triangle_idx(graph,n)
	edge_list = get_edge_list(graph,n)
	prev_triangle_idx = curr_triangle_idx
	idx = 0
	while curr_triangle_idx < frustration_limit:
		(i,j) = edge_list[idx]
		idx += 1
		
		graph[i][j] = (-1)*graph[i][j]
		
		curr_triangle_idx = calc_triangle_idx(graph,n)
		if prev_triangle_idx < curr_triangle_idx:
			yield curr_triangle_idx
			prev_triangle_idx = curr_triangle_idx
			
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

	expected_frustration = 0.8
	triangle_idx_list = []
	for triangle_idx in gen_frustration_by_edge(graph,n,expected_frustration):
		print(graph)
		triangle_idx_list.append(triangle_idx)
		
	
	print(graph)
	print(triangle_idx_list)

