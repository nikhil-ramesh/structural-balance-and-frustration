"""
This module is used for plotting bifurcation diagrams, time series and null clines.
"""
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import copy
import ode_solver

labels = ['a','b','theta','k','n']
###############################################################################
def plot_stable_attractors(graph,n,param_list,param_idx,state_idx):
	global labels
	
	num_params = 100
	num_initial_conditions = 100
	dp = 0.01
	_param_list = copy.deepcopy(param_list)
	
	fig = plt.figure()
	
	for __ in range(num_params):
		#print _param_list
		for __ in range(num_initial_conditions):
			yi = [random.uniform(0.1,2) for __ in range(n)]
			all_y,t = ode_solver.integrate_equations(yi,graph,n,_param_list)
			yf = all_y[len(all_y)-1]
			plt.plot(_param_list[param_idx], yf[state_idx],'bs')
			
		_param_list[param_idx] += dp
		
	
	plt.ylabel('y' + str(state_idx+1) + ' Fixed Points')
	plt.xlabel(str(labels[param_idx]))
	plot_name = str(n) + '_' + 'y' + str(state_idx+1) + 'vs' + labels[param_idx] + '_' + 'attractor'+ '.jpg'
	return fig,plot_name
###############################################################################
def plot_time_series(graph,n,param_list,param_idx,state_idx):
	
	num_initial_conditions = 100
	
	fig = plt.figure()
	
	for __ in range(num_initial_conditions):
		yi = [random.uniform(0.1,2) for __ in range(n)]
		all_y,t = ode_solver.integrate_equations(yi,graph,n,param_list)
		y_state_idx = np.mat(all_y).transpose().tolist()[state_idx] 
		plt.plot(t, y_state_idx)
			
	plt.ylabel('y' + str(state_idx+1))
	plt.xlabel('t')
	plot_name = str(n) + '_' + 'y' + str(state_idx+1) + 'vst' + '_' + 'time_series'+ '.jpg'
	
	return fig,plot_name	 
###############################################################################
def plot_nullclines(graph,n,param_list,param_idx,state_idx):
	global labels
	
	max_iters = 1000
	tol = 0.001
	num_params = 100
	num_initial_conditions = 100
	dp = 0.01
	_param_list = copy.deepcopy(param_list)
	
	fig = plt.figure()
	
	for __ in range(num_params):
		for __ in range(num_initial_conditions):
			iters = 0
			y = [random.uniform(0.1,2) for __ in range(n)]
			
			while True:
				jac = ode_solver.jac(y,graph,n,_param_list)				
				jac_inverse = np.linalg.matrix_power(jac,-1)
				f_y = ode_solver.f(y,0,graph,n,_param_list)
				y_prime = y - np.matmul(jac_inverse,f_y)
				f_y_prime = ode_solver.f(y_prime,0,graph,n,_param_list)
				
				if np.linalg.norm(f_y_prime) > np.linalg.norm(f_y):
					y_prime = y + 2*np.matmul(jac_inverse,f_y)
					
				y = copy.deepcopy(y_prime)
				
				if np.linalg.norm(ode_solver.f(y,0,graph,n,_param_list)) < tol:
					plt.plot(_param_list[param_idx], y[state_idx],'ro')
					break
				if iters > max_iters:
					break
					
				iters += 1

		_param_list[param_idx] += dp
		
	plt.ylabel('y' + str(state_idx+1) + ' Fixed Points')
	plt.xlabel(str(labels[param_idx]))
	plot_name = str(n) + '_' + 'y' + str(state_idx+1) + 'vs' + labels[param_idx] + '_' + 'nullclines'+ '.jpg'
	return fig,plot_name
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
		
	
	param_list = [1,1,1,1,4]
	state_idx = 0
	m = len(param_list)
	for param_idx in range(m):
		param_list = [1,1,1,1,4]
		if param_idx != 4:	
			param_list[param_idx] = 0.2
		else:
			param_list[param_idx] = 0.8
	
	
		fig,plot_name = plot_stable_attractors(graph,n,param_list,param_idx,state_idx)
		plot_name = 'f_full_' + plot_name
		fig.savefig(plot_name)
		
		
