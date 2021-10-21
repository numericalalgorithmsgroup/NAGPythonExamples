[![NAG Logo](../nag_logo.png)](https://www.nag.com)

# Local Optimization<a name=top></a>

See full offering of solvers at https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html
(modern solvers are identified with "handle_solve" prefix.)

## LP

### Sparse LP

 * IPM: e04mt (handle_solve_lp_ipm)
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.handle_solve_lp_ipm.html#naginterfaces.library.opt.handle_solve_lp_ipm
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.handle_solve_lp_ipm_ex.main
   Demo: https://github.com/numericalalgorithmsgroup/NAGPythonExamples/blob/master/local_optimization/Modelling/LP_demo.ipynb
   Demo: https://github.com/numericalalgorithmsgroup/NAGPythonExamples/blob/master/local_optimization/Modelling/production_planning.ipynb 

 * Primal-Simplex AS e04nc (qpconvex2_sparse_solve)
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.qpconvex2_sparse_solve.html#naginterfaces.library.opt.qpconvex2_sparse_solve
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.qpconvex2_sparse_solve_ex.main

### Dense LP

 * AS e04mf (lp_solve)
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.lp_solve.html#naginterfaces.library.opt.lp_solve

 * AS e04nc (lsq_lincon_solve) (also solves Convex QP)
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.lsq_lincon_solve.html#naginterfaces.library.opt.lsq_lincon_solve


## QP

### Sparse QP

 * AS e04nq (qpconvex2_sparse_solve) (convex)
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.qpconvex2_sparse_solve.html#naginterfaces.library.opt.qpconvex2_sparse_solve

 * IPM e04st (handle_solve_ipopt) (convex, possibly also nonconvex)
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.handle_solve_ipopt.html#naginterfaces.library.opt.handle_solve_ipopt
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.handle_solve_ipopt_ex.main

### Convex QCQP

 * Solver of choice: e04pt (SOCP) (handle_solve_socp_ipm)
   Doc:     https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.handle_solve_socp_ipm.html#naginterfaces.library.opt.handle_solve_socp_ipm
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.handle_solve_socp_ipm_ex.main
   Demo:    https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/local_optimization/SOCP

### Dense QP

 * AS e04nf (qp_dense_solve) (convex, possibly also nonconvex)
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.qp_dense_solve.html#naginterfaces.library.opt.qp_dense_solve
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.qpconvex2_sparse_solve_ex.main

 * AS e04nc (lsq_lincon_solve) (Convex)
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.lsq_lincon_solve.html#naginterfaces.library.opt.lsq_lincon_solve


## NLP

### Sparse

 * AS SQP (FD) e04vh (nlp2_sparse_solve)
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.nlp2_sparse_solve.html#naginterfaces.library.opt.nlp2_sparse_solve
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.nlp2_sparse_solve_ex.main

 * IPM (no-FD) e04st (handle_solve_ipopt)
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.handle_solve_ipopt.html#naginterfaces.library.opt.handle_solve_ipopt
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.handle_solve_ipopt_ex.main

 * CG AS (FD) (only bound constraints) (handle_solve_bounds_foas) (also works on dense)
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.handle_solve_bounds_foas.html#naginterfaces.library.opt.handle_solve_bounds_foas
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.handle_solve_bounds_foas_ex.main
   Demo: https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/local_optimization/FOAS

 * DFNO Model-based e04jd (handle_solve_dfno) (no derivatives required, solver of choice is problem is noisy)
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.handle_solve_dfno.html#naginterfaces.library.opt.handle_solve_dfno
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.handle_solve_dfno_ex.main
   Demo: https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/local_optimization/DFO

 * AS SQP e04ug (nlp1_sparse_solve)
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.nlp1_sparse_solve.html#naginterfaces.library.opt.nlp1_sparse_solve
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.nlp1_sparse_solve_ex.main

### Dense

 * AS SQP (FD) e04uc (nlp1_solve)
   Doc: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.nlp1_solve.html#naginterfaces.library.opt.nlp1_solve
   Example: https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#naginterfaces.library.examples.opt.nlp1_solve_ex.main




