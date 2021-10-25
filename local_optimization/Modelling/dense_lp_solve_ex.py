#!/usr/bin/env python

# Example to solve dense LP problem using (e04mf/lp_solve)

# Solve the problem
#        min      cvec^T * x
# subject to      bl <= A * x <= bu
# and if present: blx <= x <= bux

from naginterfaces.library import opt
from naginterfaces.base import utils
import numpy as np

print('naginterfaces.library.opt.lp_solve Python Example Results.')
print('Solve a small dense LP problem.')

infty = 1.0E+25

# Problem size
n = 7

# Number of linear constraints
nclin = 7

# Cost vector
cvec = np.array([-0.02, -0.20, -0.20, -0.20, -0.20,  0.04,  0.04])

# Block of linear constraints (Matrix A)
a = np.array([
[ 1.00,  1.00,  1.00,  1.00,  1.00,  1.00,  1.00,],
[ 0.15,  0.04,  0.02,  0.04,  0.02,  0.01,  0.03,],
[ 0.03,  0.05,  0.08,  0.02,  0.06,  0.01,  0.00,],
[ 0.02,  0.04,  0.01,  0.02,  0.02,  0.00,  0.00,],
[ 0.02,  0.03,  0.00,  0.00,  0.01,  0.00,  0.00,],
[ 0.70,  0.75,  0.80,  0.75,  0.80,  0.97,  0.00,],
[ 0.02,  0.06,  0.08,  0.12,  0.02,  0.01,  0.97 ] ])

# Bounds on the linear constraints
bl = np.array([-0.01, -0.10,-0.01,-0.04,-0.10, -0.01, -0.01, -0.13,  -infty,  -infty,  -infty,  -infty, -9.92E-2,-3.0E-3])
bu = np.array([ 0.01,  0.15, 0.03, 0.02, 0.05, infty, infty, -0.13, -4.9E-3, -6.4E-3, -3.7E-3, -1.2E-3,    infty, 2.0E-3])

# Initial Guess
x = np.array([-0.01, -0.03,  0.00, -0.01, -0.10,  0.02,  0.01])

# Init solver
comm = opt.nlp1_init('lp_solve')

# Increase printing verbosity
opt.lp_option_string('Print Level = 2', comm)

# Defile io manager
iom = utils.FileObjManager(locus_in_output=False)

# Solve the problem
ret = opt.lp_solve(bl, bu, x, comm, a=a, cvec=cvec, istate=None, io_manager=iom)

# Report the solution and Lagrange multipliers if solved correctly
print('id  V      Value  Lagr Mult')
for id in range(n):
    print('{:5} {: 9.3e} {: 9.3e}'.format(id+1, ret.x[id], ret.clamda[id]))

print('id LC      Value  Lagr Mult')
for id in range(nclin):
    print('{:5} {: 9.3e} {: 9.3e}'.format(n+id+1, ret.ax[id], ret.clamda[n+id]))

print('Objective value at solution {:0.5f}'.format(ret.obj))
