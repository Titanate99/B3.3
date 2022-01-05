#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 14:24:33 2021

@author: nate_mac
"""
"""
Ivp_solve = initial valbue problem, 
State vector specifies stateof system completely
2nd order equation requires 2 dimensions or 'states' 

So we'd say Q = (x,y) then dQ/dt = [x. , y.] 

For harmonic oscilator if we plot a 'state space'

plotting velocity versus position, we get an elipse!

this makes sense as....

Damped, driven harmoc oscilator

E= 1/2mv^2 +1/2kx^2

the energy of kinetic and spring
also resemlbes formula for an elipse


Attractors are geometric structures on which the dynamicaltrajectories lie

Geometrical and algeebraic constraints both represent dynamics

we only ever need/care about state vector as function of time
is an accurate way to compare your system/code to another person's 

"""
##Function minimization using matrix algebra

Input: [x,y,z]
Output: [y,z,-Az-y+|x|-1] ##[x. , y. , z.]