![NAG Logo](./nag_logo.png)<a name=top></a>

# Content<a name=content></a>

* [Examples using the NAG Library for Python](#examples)
* [How to install the NAG Library for Python](#install)
* [How to run the Jupyter notebook examples](#jupyter)
* [List of Chapters in the NAG Library for Python](#chapters)
* [Useful links](#links)

# Examples using the NAG Library for Python <a name=examples></a>

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

# How to install the NAG Library for Python<a name=install></a>

In this section we illustrate how to install the NAG Library for Python, request a Trial Licence and make sure the Library is working. Details and further information regarding the installation can be found [here](https://www.nag.com/numeric/py/nagdoc_latest/readme.html#installation).

**Note** Before starting make sure you have access to a host that has Python 3 (3.4 or more recent).

### Step 1. Downloading and installing
Installing the NAG Library is done using the `pip` package manager, fire-up a terminal and create a Python 3 virtual environment where to install and test the NAG Library
```{bash}
guest@nag-37:~$ python3 -m venv nag3
guest@nag-37:~$ . nag3/bin/activate
(nag3) guest@nag-37:~$
```
Now use `pip` to install the NAG Library for Python
```{bash}
(nag3) guest@nag-37:~$ python -m pip install --extra-index-url https://www.nag.com/downloads/py/naginterfaces_nag naginterfaces
```
or if you prefer the version of the package that relies on Intel MKL for optimized linear algebra routines, then use
```{bash}
(nag3) guest@nag-37:~$ python -m pip install --extra-index-url https://www.nag.com/downloads/py/naginterfaces_mkl naginterfaces
```

The output should be similar to
```{bash}
Collecting naginterfaces
  Downloading https://www.nag.com/downloads/py/naginterfaces_nag/naginterfaces/naginterfaces-27.1.0.0-py2.py3-none-linux_x86_64.whl (55.8MB)
    100% |████████████████████████████████| 55.8MB 21kB/s 
Collecting numpy>=1.15 (from naginterfaces)
  Downloading https://files.pythonhosted.org/packages/45/b2/6c7545bb7a38754d63048c7696804a0d947328125d81bf12beaa692c3ae3/numpy-1.19.5-cp36-cp36m-manylinux1_x86_64.whl (13.4MB)
    100% |████████████████████████████████| 13.4MB 70kB/s 
Installing collected packages: numpy, naginterfaces
Successfully installed naginterfaces-27.1.0.0 numpy-1.19.5
```
The output indicates that the installation was successful.

### Step 2. Getting a trial licence
The next step is to get the licensing info (**product code** and **KUSARI ID**) and use it to request a licence. From the same virtual terminal, try
```{bash}
(nag3) guest@nag-37:~$ python -m naginterfaces.kusari
```
The output should be similar to
```
The NAG Library for Python on this platform uses
underlying Library NLL6I271VL.
This Library has been installed as part of the package
and it requires a valid licence key.
No such key could be validated:
the key may not have been installed correctly or
it may have expired.
The Kusari licence-check utility reports the following:
User: guest
Directory: /home/guest
NAG_KUSARI_FILE=""
File /home/guest/nag.key does not exist
-------------------------------------------------------------------------------
Error: Licence not found; this product requires a key for NLL6I271VL
The above information has been generated on machine nag-37
For information on how to obtain a licence, please see
https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.kusari.html
KUSARI ID = "ADLXt-adEclJLmvnxlrU2sseteZoo,RopA-Ld"
```
The **two** important bits are the 

 1. **product code** shown as **`underlying Library NLL6I271VL.`** which identifies the licence to request, and
 
 2. **KUSARI ID** shown as **`KUSARI ID = "ADLXt-adEclJLmvnxlrU2sseteZoo,RopA-Ld"`** which identifies the host you are running the library on.
 
 **Note** that the **product code** and **KUSARI ID** can be different from the previous example.
 
 With these, you are set to [contact NAG and request a trial licence](https://www.nag.com/content/software-trials?product=NAG%20Library).
 
 The trial licence is a plain text chunk similar to
 ```
 NLL6I271V TRIAL 2021/01/27 "RverXn0Pc-Ib?ctdgF=Wpis2j7I"
 ```
 Save or copy the text into the file `/home/guest/nag.key`.
 
 The final step is to make sure the licence is valid and the library is working as expected.
 
### Step 3. Testing the NAG Library
The last step is to make sure the licence was correctly stored and that the NAG Library is working correctly. From the same virtual terminal re-run the Kusari licence module
```{bash}
(nag3) guest@nag-37:~$ python -m naginterfaces.kusari
``` 
This time the output should be similar to
```
Licence available; the required NLL6I271VL licence key for this product is valid
TRIAL licence, 27 days remaining (licence from file)
```
Now let's try a more interesting example ([list of optimization examples](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#examples))

This command runs the example for the [FOAS (First-Order Active set method) solver and minimizes the Rosenbrock 2D function](./FOAS).
```
(nag3) guest@nag-37:~$ python -m naginterfaces.library.examples.opt.handle_solve_bounds_foas_ex
```
Should generate an outputsimilar to
```{bash}
Trying:
    main()
Expecting:
    naginterfaces.library.opt.handle_solve_bounds_foas Python Example Results.
    Minimizing a bound-constrained Rosenbrock problem.
     E04KF, First order method for bound-constrained problems
...
     Status: converged, an optimal solution was found
     Value of the objective             4.00000E-02
    ...
ok
```
indicating that the example was successfully executed. The source code can be found [here](https://www.nag.com/numeric/py/nagdoc_latest/_modules/naginterfaces/library/examples/opt/handle_solve_bounds_foas_ex.html#main).

### Running more examples

To display the full list of example source files on disk, but not run them, execute
```
python -m naginterfaces.library.examples --locate
```
All examples may be executed sequentially by running
```
python -m naginterfaces.library.examples
```
Run `python -m naginterfaces.library.examples --help` to see any additional usage.



# How to run the Jupyter notebook examples<a name=jupyter></a>

This section briefly illustrates how to setup a host in order to open and run the [Jupyter notebooks](https://jupyter.org/) provided in this repository.
Before running the notebooks make sure the [NAG Library is installed and working](#install). Before starting, it is advised to read [Jupyter's installation page](https://jupyter.org/install.html).

<!-- You can [view a static render of the notebooks using Jupyter's nbviewer here](https://nbviewer.jupyter.org/github/numericalalgorithmsgroup/NAGPythonExamples/tree/master/local_optimization/) 
[![Jupyter](https://img.shields.io/badge/launch-nbviewer-blue?logo=jupyter&logoColor=white)](https://nbviewer.jupyter.org/github/numericalalgorithmsgroup/NAGPythonExamples/tree/master/local_optimization/)
or alternatively use [Binder](https://mybinder.org/) to [view them here](https://mybinder.org/v2/gh/numericalalgorithmsgroup/NAGPythonExamples/HEAD) 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/numericalalgorithmsgroup/NAGPythonExamples/HEAD). -->


### Installing Jupyter notebook
To install Jupyter, launch a terminal and activate the virtual environment used to install the NAG Library for Python
```{bash}
guest@nag-37:~$ . nag3/bin/activate
(nag3) guest@nag-37:~$ pip install notebook matplotlib
Collecting notebook
  Downloading https://files.pythonhosted.org/packages/74/19/50cd38acf22e33370d01fef764355f1e3517f6e12b4fceb8d434ece4f8fd/notebook-6.2.0-py3-none-any.whl (9.5MB)
    100% |████████████████████████████████| 9.5MB 115kB/s 
Collecting argon2-cffi (from notebook)
...
Successfully installed jupyter-client-6.1.11 jupyterlab-pygments-0.1.2 ... wcwidth-0.2.5
```
This indicates that Jupyter and matplotlib were successfully installed. The next section shows how to start the notebok interface and open an example.

### Running the notebook examples
To run an example, grab a copy of the notebook of interest and start up the notebook interface.
For example, download the [Rosenbrock 2D optimization example](./FOAS/rosenbrock2d.ipynb) notebook `rosenbrock2d.ipynb` into the current directory
```{bash}
(nag3) guest@nag-37:~$ curl -O https://raw.githubusercontent.com/numericalalgorithmsgroup/NAGPythonExamples/master/local_optimization/FOAS/rosenbrock2d.ipynb
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 61961  100 61961    0     0   382k      0 --:--:-- --:--:-- --:--:--  382k
```
and now open it using `jupyter-notebook`
```{bash}
(nag3) guest@nag-37:~$ jupyter-notebook rosenbrock2d.ipynb
[I 12:24:07.336 NotebookApp] Serving notebooks from local directory: /home/guest
[I 12:24:07.336 NotebookApp] Jupyter Notebook 6.2.0 is running at:
[I 12:24:07.336 NotebookApp] http://localhost:8888/?token=f1836a06799a92f25ef9966439bf3491b2f0960dcb51806d
...
```
This command will fire-up your web browser and open the `rosenbrock2d.ipynb` notebook, the window should be similar to


![Notebook screenshot](local_optimization/images/screenshot.png)



# List of Chapters in the NAG Library for Python<a name=chapters></a>

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


# Useful links<a name=links></a>

* [NAG Library for Python Documentation](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html)
* [Request a trial licence](https://www.nag.com/content/software-trials?product=NAG%20Library)
* [Kusari licence module Documentation](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.kusari.html#kusari)


**[Back to Top](#top)**
