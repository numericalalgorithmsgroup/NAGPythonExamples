![NAG Logo](./nag_logo.png)

# Examples using the NAG Library for Python

This repository contains examples and demonstrations using the [NAG Library for Python](https://www.nag.co.uk/nag-library-python).  The NAG Library for Python contains 1700+ functions spanning many areas of numerical computing and data science.  

Designed to work alongside the open source Python packages, [Numpy](http://www.numpy.org/) and [Scipy](https://www.scipy.org/), The NAG Library for Python can augment your computational workflow in many areas.

## Directory of examples

* [Local optimisation](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/local_optimisation)
* [Global Optimisation](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/global_optimisation)
* [Operations Research](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/operations_research)
* [Correlation and regression analysis](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/correlation_and_regression_analysis)
* [Multivariate methods](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/multivariate_methods)
* [Random number generation](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/random_number_generation)
* [Curve and surface fitting](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/curve_and_surface_fitting)
* [Time series analysis](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/time_series_analysis)
* [Neareast Correlation Matrices](https://github.com/numericalalgorithmsgroup/NAGPythonExamples/tree/master/neareast_correlation_matrices)

## NAG library for Python installation

The NAG library for Python comes in two versions. One is linked to the Intel MKL for improved linear algebra performance on x86 architectures and the other is linked to NAG's self contained linear algebra libraries.

When using Intel or AMD CPUs we recommend the use of the Intel MKL version of the NAG Library for Python. 

Install using the following command

```
python -m pip install --extra-index-url https://www.nag.com/downloads/py/naginterfaces_mkl naginterfaces
```

**Obtaining a license** 

Before you can use the NAG Library for Python, you'll need a license.  Free trial licenses are available!

Run the following command to begin the licensing process and email [support@nag.co.uk](mailto:support@nag.co.uk?subject=License for NAG Library for Python) if you have any problems.

```
# This will launch a license request GUI on windows
# On Mac and Linux, it gives the information you need to send to support@nag.co.uk in order to request a trial license
python -m naginterfaces.kusari
```

* More detailed installation instructions are [available in the official documentation](https://www.nag.co.uk/numeric/py/nagdoc_latest/readme.html#installation).
* More detailed license management instructions are available at [https://www.nag.co.uk/numeric/py/nagdoc_latest/naginterfaces.kusari.html#kusari](https://www.nag.co.uk/numeric/py/nagdoc_latest/naginterfaces.kusari.html#kusari)
