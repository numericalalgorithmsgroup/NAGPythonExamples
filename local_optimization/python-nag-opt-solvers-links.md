[![NAG Logo](../nag_logo.png)](https://www.nag.com)

# Local Optimization<a name=top></a>

See full offering of solvers at https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html
(modern solvers are identified with "handle_solve" prefix.)

## LP

### Sparse LP

 * IPM: e04mt (handle_solve_lp_ipm)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.handle_solve_lp_ipm.html#naginterfaces.library.opt.handle_solve_lp_ipm</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.handle_solve_lp_ipm_ex.main</br>
   Demo: https://github.com/numericalalgorithmsgroup/NAGPythonExamples/blob/master/local_optimization/Modelling/LP_demo.ipynb</br>
   Demo: https://github.com/numericalalgorithmsgroup/NAGPythonExamples/blob/master/local_optimization/Modelling/production_planning.ipynb </br>

 * Primal-Simplex AS e04nc (qpconvex2_sparse_solve)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.qpconvex2_sparse_solve.html#naginterfaces.library.opt.qpconvex2_sparse_solve</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.qpconvex2_sparse_solve_ex.main</br>

### Dense LP

 * AS e04mf (lp_solve)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.lp_solve.html#naginterfaces.library.opt.lp_solve</br>

 * AS e04nc (lsq_lincon_solve) (also solves Convex QP)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.lsq_lincon_solve.html#naginterfaces.library.opt.lsq_lincon_solve</br>


## QP

### Sparse QP

 * AS e04nq (qpconvex2_sparse_solve) (convex)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.qpconvex2_sparse_solve.html#naginterfaces.library.opt.qpconvex2_sparse_solve</br>

 * IPM e04st (handle_solve_ipopt) (convex, possibly also nonconvex)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.handle_solve_ipopt.html#naginterfaces.library.opt.handle_solve_ipopt</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.handle_solve_ipopt_ex.main</br>

### Convex QCQP (SOCP)

 * Solver of choice: e04pt (SOCP) (handle_solve_socp_ipm)</br>
   Doc:     https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.handle_solve_socp_ipm.html#naginterfaces.library.opt.handle_solve_socp_ipm</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.handle_solve_socp_ipm_ex.main</br>
   Demo:    https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/local_optimization/SOCP</br>

### Dense QP

 * AS e04nf (qp_dense_solve) (convex, possibly also nonconvex)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.qp_dense_solve.html#naginterfaces.library.opt.qp_dense_solve</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.qpconvex2_sparse_solve_ex.main</br>

 * AS e04nc (lsq_lincon_solve) (Convex)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.lsq_lincon_solve.html#naginterfaces.library.opt.lsq_lincon_solve</br>


## NLP

### Sparse

 * AS SQP (FD) e04vh (nlp2_sparse_solve)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.nlp2_sparse_solve.html#naginterfaces.library.opt.nlp2_sparse_solve</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.nlp2_sparse_solve_ex.main</br>

 * IPM (no-FD) e04st (handle_solve_ipopt)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.handle_solve_ipopt.html#naginterfaces.library.opt.handle_solve_ipopt</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.handle_solve_ipopt_ex.main</br>

 * CG AS (FD) (only bound constraints) (handle_solve_bounds_foas) (also works on dense)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.handle_solve_bounds_foas.html#naginterfaces.library.opt.handle_solve_bounds_foas</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.handle_solve_bounds_foas_ex.main</br>
   Demo: https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/local_optimization/FOAS</br>

 * DFNO Model-based e04jd (handle_solve_dfno) (no derivatives required, solver of choice is problem is noisy)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.handle_solve_dfno.html#naginterfaces.library.opt.handle_solve_dfno</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.handle_solve_dfno_ex.main</br>
   Demo: https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/local_optimization/DFO</br>

 * AS SQP e04ug (nlp1_sparse_solve)
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.nlp1_sparse_solve.html#naginterfaces.library.opt.nlp1_sparse_solve</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.nlp1_sparse_solve_ex.main</br>

### Dense

 * AS SQP (FD) e04uc (nlp1_solve)</br>
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.nlp1_solve.html#naginterfaces.library.opt.nlp1_solve</br>
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.nlp1_solve_ex.main</br>




