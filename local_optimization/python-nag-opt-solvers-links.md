[![NAG Logo](../nag_logo.png)](https://www.nag.com)

# Local Optimization<a name=top></a>

See full offering of solvers at 
https://www.nag.com/numeric/nl/nagdoc_latest/flhtml/indexes/optimization.html </br>
(https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html)
NOMS solvers are identified with "handle_solve" prefix.

**Abbreviations used**

|Abbreviation     | Description  |
|--------|--------------|
| (FD)   | Indicates the solver does not require the user to provide 1st order derivativas and in which case it will use a Finite-Difference method to estimate them |
| (no-FD)| Indicates that the solver requires the user to provide derivates|
| AS     | Active-Set Method
| DFNO   | Derivative-Free Nonlinear Programming 
| IPM    | Interior-Point Method
| LP     | Linear Programming
| NLP    | Nonlinear Programming
| QCQP   | Quadratically-constrained Quadratic Programming
| QP     | Quadratic Programming
| SOCP   | Second-Order Cone Programming
| SQP    | Sequential Quadratic Programming

## LP

### Sparse LP

 * IPM: `e04mt (handle_solve_lp_ipm)`</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.handle_solve_lp_ipm.html#naginterfaces.library.opt.handle_solve_lp_ipm</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.handle_solve_lp_ipm_ex.main</br>
   Demo: https://github.com/numericalalgorithmsgroup/NAGPythonExamples/blob/master/local_optimization/Modelling/LP_demo.ipynb</br>
   Demo: https://github.com/numericalalgorithmsgroup/NAGPythonExamples/blob/master/local_optimization/Modelling/production_planning.ipynb </br>

 * Primal-Simplex AS `e04nc (qpconvex2_sparse_solve)`</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.qpconvex2_sparse_solve.html#naginterfaces.library.opt.qpconvex2_sparse_solve</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.qpconvex2_sparse_solve_ex.main</br>

### Dense LP

 * AS `e04mf (lp_solve)`</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.lp_solve.html#naginterfaces.library.opt.lp_solve</br>

 * AS `e04nc (lsq_lincon_solve)` (also solves convex QP)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.lsq_lincon_solve.html#naginterfaces.library.opt.lsq_lincon_solve</br>


## QP

### Sparse QP

 * AS `e04nq (qpconvex2_sparse_solve)` (convex)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.qpconvex2_sparse_solve.html#naginterfaces.library.opt.qpconvex2_sparse_solve</br>

 * IPM `e04st (handle_solve_ipopt)` (convex, possibly also nonconvex)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.handle_solve_ipopt.html#naginterfaces.library.opt.handle_solve_ipopt</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.handle_solve_ipopt_ex.main</br>

### Convex QCQP (SOCP)

 * Solver of choice: `e04pt (handle_solve_socp_ipm)`</br>
   Doc:     https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.handle_solve_socp_ipm.html#naginterfaces.library.opt.handle_solve_socp_ipm</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.handle_solve_socp_ipm_ex.main</br>
   Demo:    https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/local_optimization/SOCP</br>

### Dense QP

 * AS `e04nf (qp_dense_solve)` (convex, possibly also nonconvex)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.qp_dense_solve.html#naginterfaces.library.opt.qp_dense_solve</br>

 * AS `e04nc (lsq_lincon_solve)` (convex)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.lsq_lincon_solve.html#naginterfaces.library.opt.lsq_lincon_solve</br>


## NLP

### Sparse

 * SQP AS (FD) `e04sr (handle_solve_ssqp)` (Mark 28.3 / 28.4)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.handle_solve_ssqp.html#naginterfaces.library.opt.handle_solve_ssqp</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/_modules/naginterfaces/library/examples/opt/handle_solve_ssqp_ex.html#main</br>

 * SQP AS (FD) `e04vh (nlp2_sparse_solve)`</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.nlp2_sparse_solve.html#naginterfaces.library.opt.nlp2_sparse_solve</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.nlp2_sparse_solve_ex.main</br>

 * IPM (no-FD) `e04st (handle_solve_ipopt)`</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.handle_solve_ipopt.html#naginterfaces.library.opt.handle_solve_ipopt</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.handle_solve_ipopt_ex.main</br>

 * Conjugate Gradient AS (FD) (only bound constraints) `e04kf (handle_solve_bounds_foas)` (also works on dense)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.handle_solve_bounds_foas.html#naginterfaces.library.opt.handle_solve_bounds_foas</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.handle_solve_bounds_foas_ex.main</br>
   Demo: https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/local_optimization/FOAS</br>

 * DFNO Model-based `e04jd (handle_solve_dfno)` (no derivatives required, solver of choice is problem is noisy)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.handle_solve_dfno.html#naginterfaces.library.opt.handle_solve_dfno</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.handle_solve_dfno_ex.main</br>
   Demo: https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/local_optimization/DFO</br>

 * SQP AS `e04ug (nlp1_sparse_solve)`
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.nlp1_sparse_solve.html#naginterfaces.library.opt.nlp1_sparse_solve</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.nlp1_sparse_solve_ex.main</br>

### Dense

 * SQP AS (FD) `e04uc (nlp1_solve)`</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.nlp1_solve.html#naginterfaces.library.opt.nlp1_solve</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.nlp1_solve_ex.main</br>




