#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 14:48:54 2022

@author: nate_mac
"""

import matplotlib.pyplot as plt

#same pendulum problem, but now theres friction damping, oh and a motor


# we now just need to change our equation for a, 'omega'
#omega_naught, is natural frequency of the pendulum
#w_0 =g/L

#damped, driven system is reduced to drive frequency over time. All starting energy is taken
import matplotlib.pyplot as plt

L=5
N = 2000
g = 9.8 #m/s^2
beta = 0.5
gamma =1.47
w_0 = (g/L)**(1/2)
w_drive = 1.2 * w_0 #constant times natural frequency



#if we want 1000 points in 1 second
Theta = np.zeros(N)
#starting position
Theta[0] = 1

ThetaDot = np.zeros(N)
ThetaDot[0] = 0

w = np.zeros(N)
#starting velocity
w[0] = 0


#for time of 1 second
t = np.linspace(0,30,N)
dt = t[1] - t[0]

for n in range(1,N):
    a = - ((w_0**(2)) * np.sin(Theta[n-1])) - (2*beta*w[n-1]) + (gamma*(w_0**(2))* np.cos(w_drive * t[n-1]))
    ThetaDot[n] = a
    w[n] = w[n-1] + a * dt
    Theta[n] = Theta[n-1] + w[n]*dt
    
print("Beta is: " + str(beta))
print("Gamma is: " + str(gamma))
#plt.plot(t,Theta)
plt.plot(Theta, ThetaDot)
