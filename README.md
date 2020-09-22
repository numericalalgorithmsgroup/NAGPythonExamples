![NAG Logo](./nag_logo.png)

# Examples using the NAG Library for Python

**Example Edit**

This repository contains examples and demonstrations using the [NAG Library for Python](https://www.nag.com/nag-library-python).  The NAG Library for Python contains 1900+ functions spanning many areas of numerical computing and data science.

Designed to work alongside the open source Python packages, [Numpy](http://www.numpy.org/) and [Scipy](https://www.scipy.org/), The NAG Library for Python can augment your computational workflow in many areas.

## Directory of GitHub examples

* [Correlation and regression analysis](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/correlation_and_regression_analysis)
* [Curve and surface fitting](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/curve_and_surface_fitting)
* [Dimensionality Reduction](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/dimension_reduction)
* [Global Optimization](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/global_optimization)
* [Linear Algebra](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/linear_algebra)
* [Local optimization](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/local_optimization)
* [Multivariate methods](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/multivariate_methods)
* [Nearest Correlation Matrices](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/nearest_correlation_matrices)
* [Operations Research](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/operations_research)
* [Random number generation](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/random_number_generation)
* [Roots](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/roots)
* [Time series analysis](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/time_series_analysis)

## Examples that ship with the product

In addition to those presented here, The NAG Library for Python ships with a set of usage examples.  To see them all, run the following command

```
python -m naginterfaces.library.examples --locate
```

## NAG Library for Python installation

The NAG Library for Python comes in two versions. One is linked to the Intel MKL for improved linear algebra performance on x86 architectures and the other is linked to NAG's self contained linear algebra libraries.

When using Intel or AMD CPUs we recommend the use of the Intel MKL version of the NAG Library for Python.

Install using the following command

```
python -m pip install --extra-index-url https://www.nag.com/downloads/py/naginterfaces_mkl naginterfaces
```

## Obtaining a license

Before you can use the NAG Library for Python, you'll need a license.  Free trial licenses are available!

Run the following command to begin the licensing process and email [support@nag.com](mailto:support@nag.com) if you have any problems.

```
# This will launch a license request GUI on windows
# On Mac and Linux, it gives the information you need to send to support@nag.com to request a trial license
python -m naginterfaces.kusari
```

* More detailed installation instructions are [available in the official documentation](https://www.nag.com/numeric/py/nagdoc_latest/readme.html#installation).
* More detailed license management instructions are available at [https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.kusari.html#kusari](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.kusari.html#kusari)

## List of Chapters in the NAG Library for Python

The following links take you to the relevant section in the official documentation

* [library.anova](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.anova.html) - Analysis of Variance
* [library.blas](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.blas.html) - Linear Algebra Support Routines
* [library.blast](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.blast.html) - Further Linear Algebra Support Routines
* [library.blgm](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.blgm.html) - Linear Model Specification
* [library.complex](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.complex.html) - Complex Arithmetic
* [library.contab](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.contab.html) - Contingency Table Analysis
* [library.correg](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.correg.html) - Correlation and Regression Analysis
* [library.det](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.det.html) - Determinants
* [library.dot](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.dot.html) - Inner Products
* [library.eigen](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.eigen.html) - Eigenvalues and Eigenvectors
* [library.fit](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.fit.html) - Curve and Surface Fitting
* [library.glopt](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.glopt.html) - Global Optimization of a Function
* [library.ieee](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.ieee.html) - IEEE Arithmetic
* [library.info](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.info.html) - Library Identification
* [library.inteq](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.inteq.html) - Integral Equations
* [library.interp](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.interp.html) - Interpolation
* [library.lapackeig](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.lapackeig.html) - Least Squares and Eigenvalue Problems
* [library.lapacklin](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.lapacklin.html) - Linear Equations
* [library.linsys](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.linsys.html) - Simultaneous Linear Equations
* [library.machine](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.machine.html) - Machine Constants
* [library.math](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.math.html) - Mathematical Constants
* [library.matop](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.matop.html) - Matrix Operations, Including Inversion
* [library.mesh](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.mesh.html) - Mesh Generation
* [library.mip](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.mip.html) - Operations Research
* [library.mv](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.mv.html) - Multivariate Methods
* [library.nonpar](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.nonpar.html) - Nonparametric Statistics
* [library.numdiff](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.numdiff.html) - Numerical Differentiation
* [library.ode](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.ode.html) - Ordinary Differential Equations
* [library.omp](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.omp.html) - OpenMP Utilities
* [library.opt](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html) - Minimizing or Maximizing a Function
* [library.orthog](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.orthog.html) - Orthogonalization
* [library.pde](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.pde.html) - Partial Differential Equations
* [library.quad](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.quad.html) - Quadrature
* [library.rand](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.rand.html) - Random Number Generators
* [library.rnla](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.rnla.html) - Randomized Numerical Linear Algebra
* [library.roots](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.roots.html) - Roots of One or More Transcendental Equations
* [library.smooth](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.smooth.html) - Smoothing in Statistics
* [library.sort](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.sort.html) - Sorting and Searching
* [library.sparse](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.sparse.html) - Large Scale Linear Systems
* [library.sparseig](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.sparseig.html) - Large Scale Eigenproblems
* [library.specfun](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.specfun.html) - Approximations of Special Functions
* [library.stat](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.stat.html) - Simple Calculations on Statistical Data
* [library.sum](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.sum.html) - Summation of Series
* [library.surviv](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.surviv.html) - Survival Analysis
* [library.tsa](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.tsa.html) - Time Series Analysis
* [library.univar](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.univar.html) - Univariate Estimation
* [library.wav](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.wav.html) - Wavelet Transforms
* [library.zeros](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.zeros.html) - Zeros of Polynomials
