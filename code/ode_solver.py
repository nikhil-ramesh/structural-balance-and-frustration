"""
This module integrates the system of equations given an initial state.
"""
from  scipy.integrate import odeint
import numpy as np

###############################################################################
def f(x,t,graph,n,param_list):
	[a,b,theta,k,n_exp] = param_list
    
	f_out = [0]*n
	for i in range(n):
		for j in range(n):
			if i == j:
				f_out[i] -= k*x[i]
			elif graph[i][j] == 1:
				f_out[i] += (a*(x[j]**n_exp))/((theta**n_exp)+(x[j]**n_exp))
			elif graph[i][j] == -1:
				f_out[i] += (b*(theta**n_exp))/((theta**n_exp)+(x[j]**n_exp))
                
	return f_out
###############################################################################
def jac(x,graph,n,param_list):
	n = len(x)
	
	dx = 0.001
	jac_out = [[0]*n for __ in range(n)]
	f_x = f(x,0,graph,n,param_list)
	f_x_prime = [[] for __ in range(n)]
	for i in range(n):
		x[i] += dx
		f_x_prime[i] = f(x,0,graph,n,param_list)
		x[i] -= dx
    
	for i in range(n):
		for j in range(n):
			jac_out[i][j] = (f_x_prime[j][i]-f_x[i])/dx
            
	return jac_out

###############################################################################
def integrate_equations(start_state,graph,n,param_list):
	tmax = 100
	dt = 0.1
	t = np.arange(0,tmax,dt)
	all_states = odeint(f,start_state,t,args = (graph,n,param_list))
	
	return all_states,t
###############################################################################

