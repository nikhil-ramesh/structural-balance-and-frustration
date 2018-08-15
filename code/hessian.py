"""
Module to determine the hessian of the system.
"""
#################################################################################
import numpy as np
import random as rand
from ode_solver import integrate_equations
from copy import deepcopy
##################################################################################
def get_chi_sqr(graph,n,param_list,num_rows,num_cols,dp):
	
	sigma = [0]*n
	num_conditions = 60
	for __ in range(num_conditions):
		y0 = [rand.uniform(0.1,2) for __ in range(n)]
		
		all_states,__ = integrate_equations(y0,graph,n,param_list)
		y = all_states[len(all_states) - 1]
		
		sigma = [max(sigma[i], y[i]) for i in range(n)]	
		
	p_star = deepcopy(param_list) 
	
	chi_sqr = [[0]*num_cols for __ in range(num_rows)]
	
	for i in range(num_rows):
		p = deepcopy(param_list)
		for j in range(num_cols):
			p[i] = p[i] + dp
			print p
			for __ in range(num_conditions):
				y0 = [rand.uniform(0.1,2) for __ in range(n)]
	
				all_states,__ = integrate_equations(y0,graph,n,p_star)
				y_star = all_states[len(all_states) - 1]	
				
				all_states,__ = integrate_equations(y0,graph,n,p)
				y = all_states[len(all_states) - 1]
				
				for k in range(n):
					chi_sqr[i][j] += (y_star[k] - y[k])**2/sigma[k]
		
			chi_sqr[i][j] = chi_sqr[i][j]/(n*num_conditions)
	
	return chi_sqr
##################################################################################
def get_jac(chi_sqr,m,n,dp):
	
	jac_out = [[0]*n for __ in range(m)]
	for i in range(m):
		for j in range(n):
			jac_out[i][j] = (chi_sqr[i][j+1] - chi_sqr[i][j])/dp
	
	return jac_out
##################################################################################
def get_hessian(graph,n,param_list):
	
	m = len(param_list)
	dp = 0.01
	num_points = 100
	
	chi_sqr = get_chi_sqr(graph,n,param_list,m,num_points,dp)
	jac = get_jac(chi_sqr,m,(num_points-1),dp)
	hess = np.matmul(np.mat(jac),np.mat(jac).transpose()).tolist()
	
	return hess
	
##################################################################################
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
	
	param_list = [0.2,0.2,0.2,0.2,3.5]
	hess = get_hessian(graph,n,param_list)		
	print hess		
	eig = np.linalg.eig(hess)
	print eig

