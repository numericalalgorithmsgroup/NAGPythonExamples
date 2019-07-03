[Second Order Cone Programming (SOCP)](https://en.wikipedia.org/wiki/Second-order_cone_programming) is convex optimization which extends linear programming (LP) with second-order (Lorentz or the ice cream) cones. Search region of the solution is the intersection of an affine
linear manifold with the Cartesian product of second-order cones. 

The figure below shows an example feasible region of an SOCP problem with 3 variables.

![SOCP Example](./socp_illus.png)

SOCP appears in a broad range of applications from engineering, control theory and quantitative finance to quadratic programming
and robust optimization. It has become an important tool for financial optimization due to its powerful nature. Interior point
methods (IPM) are the most popular approaches to solve SOCP problems due to their theoretical polynomial complexity and practical performance.

This directory contains demonstrations using NAG's SOCP solver in Python.

## Portfolio Optimisation using Second Order Cone Programming (SOCP)

This demonstration is a walk-through of modelling techniques in portfolio optimization using second-order cone programming in the NAG Library. Models in portfolio optimization include

* quadratic programming (efficient frontier)
* quadratically constrained quadratic programming (tev portfolio)
* optimization with objective of fraction of quadratic and linear (the Sharpe ratio).

General functions are enclosed for users to get the principle idea on SOCP reformulation. They provide one of the ways to build and solve their problems using NAG's SOCP solver and could be copy and paste into a model and reuse repeatedly.               

* [portfolio_optimisation_using_socp.ipynb](./portfolio_optimisation_using_socp.ipynb)  Jupyter notebook
* [portfolio_optimisation_using_socp.pdf](./static/portfolio_optimisation_using_socp.pdf)  Static pdf version
* [portfolio_optimisation_using_socp.html](./static/portfolio_optimisation_using_socp.html)  Static html version

## Robust linear programming in portfolio optimization using the NAG Library 

A mean-variance model with probability constraint using randomly generated data.

* [robust_lp.ipynb](./robust_lp.ipynb) Jupyter Notebook
* [robust_lp.html](./static/robust_lp.html) Static html version

# Data

* [stock_price.pkl](./stock_price.pkl) - pickled data file contains daily prices of 30 stocks in DJIA from March 2018 to March 2019. It is used to estimate out-of-sample expected return and covariance matrix.

# Poster 

A 2019 poster discussing NAG's SOCP functionality is [available on the NAG website](https://www.nag.com/market/posters/socp.pdf) 
