#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 18:00:09 2021

@author: nate_mac

Code up the damped, driven pendulum using solve_ivp from scipy.integrate.  
You'll need to define a vector function for determining the derivatives 
(review section 6.8 of K&N if need be).

In case it's handy to have it here, the equation is:

𝜃¨+2𝛽𝜃˙+𝜔20sin𝜃=𝛾𝜔20cos𝜔𝑡

where, 𝜔20=𝑔/𝐿 , 𝛽 is the damping strength, and 𝛾 is the drive strength.  
Play around with the damping, drive strength, and drive frequency.  
Make another plot to submit that shows the phase portrait (𝜃˙ vs 𝜃) for 𝛽=0.5 
and 𝛾=1.47 with 𝜔=23𝜔0 and verify that it matches your solution from
 last week (using odeint).
 
 
 all ode solvers assume it takes time, your state vector, then packaged other variables
 
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

gamma = 1

def f(t,x,omega_0,omega,beta,gamma):
    f_0 = x[1]
    f_1 = gamma * omega_0**2*np.cos(omega*t)-omega_0**2*np.sin(x[0])-2*beta*x[1]
    
    return np.array([f_0,f_1])

def oscilator(x_0,v_0,omega_0=1,omega = 1, beta = 0, gamma=0,periods=5,tau=0.1):
    T = 2 * np.pi/omega_0
    t_max = T*periods
    t= np.arange(0,t_max,tau)
    X_0 = [x_0,v_0]
    return(t, solve_ivp(f,(0,t_max), X_0, args=(omega,beta,gamma),max_step=tau))



if __name__ == '__main__':
    X=oscilator(10,0,omega_0=2,omega=4/3,beta=0.65, gamma=2.07, periods=200,tau=0.01)
    t= X.t
    x= X.y
    
    
    plot.plot(x[0],x[1],'p--')
    plt.show()
    