"""
Main module that used to compare structurally balanced vs frustrated 
"""

from introduce_frustration import make_frustrated
import plot
###############################################################################
def compare(graph,n,param_list,param_idx,state_idx,plot_choice):
	fig, plot_name = plot_choice(graph,n,param_list,param_idx,state_idx)
	plot_name = 'sb_'+plot_name
	fig.savefig(plot_name)
	min_expected_frustration = 0.5
	frustration_level = make_frustrated(graph,n,min_expected_frustration)
	print frustration_level
	fig, plot_name = plot_choice(graph,n,param_list,param_idx,state_idx)
	plot_name = 'f_'+plot_name
	fig.savefig(plot_name)	

###############################################################################
if __name__ == "__main__":
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
	
	param_list = [1,0.2,1,1,4]
	param_idx = 1
	state_idx = 0	
	compare(graph,n,param_list,param_idx,state_idx,plot.plot_nullclines)		

