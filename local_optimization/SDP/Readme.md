[![NAG Logo](../../nag_logo.png)](https://www.nag.com)

# Semi-Definite Programming (SDP)

[[`handle_solve_pennon`](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.handle_solve_pennon.html#naginterfaces.library.opt.handle_solve_pennon) | [`e04svf`](https://www.nag.co.uk/numeric/nl/nagdoc_latest/flhtml/e04/e04svf.html) | 
[`e04svc`](https://www.nag.co.uk/numeric/nl/nagdoc_latest/clhtml/e04/e04svc.html) ]


Linear semidefinite programming can be viewed as a generalization of linear programming. While keeping many good properties of LP (such as the duality theory and solvability in polynomial time), SDP introduces a new highly nonlinear type of constraint – matrix inequality. It is an inequality on the eigenvalues of a matrix which depends on the decision variables. Typically, the matrix inequality is written in the form to request all eigenvalues of the matrix to be non-negative, thus the matrix is to be positive semidefinite

* [Matrix completion using Semi-Definite Programming (SDP)](./matrix_completion.ipynb)
* [Nearest correlation matrix using Semi-Definite Programming (SDP)](./NCM_SDP.ipynb)
* [Compute the Lovasz number of a graph using Semi-Definite Programming (SDP)](./theta_optimization.ipynb)

<!-- foot banner for commercial material -->

# Obtaining the NAG Library for Python

 * Instructions on [how to install the NAG Library for Python](../Readme.md#install)
 * Instructions on [how to run the Jupyter notebooks in the Repository](../Readme.md#jupyter)
