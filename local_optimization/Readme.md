[![NAG Logo](../nag_logo.png)](https://www.nag.com)

# Local Optimization

Here you will find a variety of resources (mostly Python notebooks) related to the use of our optimization routines and modelling suite. If you are new to NAG's optimization solvers we highly recomment to read the [E04 chapter](https://www.nag.com/numeric/nl/nagdoc_latest/clhtml/e04/e04intro.html) of the [NAG](https://www.nag.com) Library which is dedicated to local optimization. While if you are new to NAG Library for Python we encourage to review the [Python documentation](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html). 

If you are already familiar with NAG's optimization offering and just need to find the right solver to use for your problem, then we recommend reviewing the [Optimization Index](https://www.nag.com/numeric/nl/nagdoc_latest/flhtml/indexes/optimization.html) or the [Decision Tree for selecting the right Optimization solver](https://www.nag.com/numeric/nl/nagdoc_latest/flhtml/e04/e04intro.html#dtree).


<table><tr>
<td><img src="./images/dfo_calib.png" width="412px" alt="DFO Calibration example"/></td>
  <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
 <td><img src="./images/wingsection.png" width="412px" alt="Optimization example of a wing section"/></td>
</tr></table>

**Figure 1.** Applied optimization examples. (left) DFO nonlinear least-square calibration for the Kowalik and Osborne function, 
red line shows the final solution. (right) Optimization of a wing section: red represent the baseline, center section in yellow 
shows an overall improvement of 13% while the rightmost section in green/blue shows a further 33% improvement. 

# Content

* [Second Order Cone Programming (SOCP)](./SOCP/)
* [First order active set CG (FOAS)](./FOAS)
* [Nonlinear Least-Squares (BXNL)](./BXNL)
* [Semi-Definite Programming (SDP)](./SDP/)
* [Derivative-Free Optimization (DFO)](./DFO/)
* [Tips and Tricks in modelling](./modelling)

## Examples (Remove)
* [Minimizing the generalized Rosenbrock function using bound constrained optimization](./bounds_quasi_func_easy.ipynb)
* [Linear Programming Demo](./LP_demo.ipynb)
* [Model-based derivative free optimization](./DFO_noisy.ipynb)

# How to install the NAG Library for Python

In this section we illustrate how to install the NAG Library for Python, request a Trial Licence and make sure the Library is working. Details and further information regarding the installation can be found [here](https://www.nag.com/numeric/py/nagdoc_latest/readme.html#installation).

### Step 1. Downloading and Installing (`pip`)
Installing the Library is done using the `pip` package manager, fire-up a terminal and create a Python 3 virtual environment where to install and test the Library
```{bash}
guest@nag-37:~$ python3 -m venv nag3
guest@nag-37:~$ . nag3/bin/activate
(nag3) guest@nag-37:~$
```

```{bash}
(nag3) guest@nag-37:~$ python -m pip install --extra-index-url https://www.nag.com/downloads/py/naginterfaces_nag naginterfaces
```
or if you have Intel MKL, then use
```{bash}
(nag3) guest@nag-37:~$ python -m pip install --extra-index-url https://www.nag.com/downloads/py/naginterfaces_mkl naginterfaces
```
for Intel MKL-enabled NAG Library.

### Step 2. Getting a Trial License
The next step is to get the licensing info (**product code** and **KUSARI ID**) and request a lincense. From the same virtual terminal
```{bash}
(nag3) andrews@olney:~$ python -m naginterfaces.kusari
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
The above information has been generated on machine olney.nag.co.uk
For information on how to obtain a licence, please see
https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.kusari.html
KUSARI ID = "ADLXt-adEclJLmvnxlrYfsseteZoo,mRLd"
```
The **two** important bits are the 

 1. **product code** shown as **`underlying Library NLL6I271VL.`** which identifies the lincense to request, and
 
 2. **Kusary ID** shown as **`KUSARI ID = "ADLXt-adEclJLmvnxlrYfsseteZoo,mRLd"`** which idenfies the machine you are running the library on.
 
 **Note** the **product code** might be different while the **Kusari ID** _will_ be different for your case.
 
 With these, you are set to [contact NAG and request a trial license](https://www.nag.com/content/software-trials?product=NAG%20Library).
 
 The trial licence is a plain text chunk similar to
 ```
 NLL6I271VL TRIAL "Xu+++XjvgmyemlussawO0+++++" "++++vylBNlEagiaouoce----" &
& "k5kissm+n+++++eyhH5gabf"
 ```
 So copy and save the text into the file `/home/guest/nag.key`.
 
 The final step is to make sure the licence is valid and the library is working as expected
 
### Step 3. Testing the Library
The last step is to make sure the licence was correctly stored and that the library is working correctly. From the same virtual terminal re-run kusary
```{bash}
(nag3) andrews@olney:~$ python -m naginterfaces.kusari
``` 
This time the output should be similar to
```
```
Let's try some other more interesting example ([list of optimization examples](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html#examples))

This command runs the example for the [FOAS (First-Order Active set method) solver and minimizes the Rosenbrock 2D function](./FOAS).
```
python -m naginterfaces.library.examples.opt.handle_solve_bounds_foas_ex
```

### Running more examples

All examples may be executed sequentially by running
```
python -m naginterfaces.library.examples
```
To display the full list of example source files on disk, but not run them, execute
```
python -m naginterfaces.library.examples --locate
```
Run
```
python -m naginterfaces.library.examples --help
```
to see any additional usage.

<!---# How to run the Jupyter notebooks examples--->

# Useful links

* [NAG Library for Python Documentation](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.library.opt.html)
* [NAG Library Optimization (Chapter E04) Introduction](https://www.nag.com/numeric/nl/nagdoc_latest/clhtml/e04/e04intro.html)
* [Optimization Index](https://www.nag.com/numeric/nl/nagdoc_latest/flhtml/indexes/optimization.html) 
* [Decision Tree for selecting the right Optimization solver](https://www.nag.com/numeric/nl/nagdoc_latest/flhtml/e04/e04intro.html#dtree)
* [Request a Trial Licence](https://www.nag.com/content/software-trials?product=NAG%20Library)
* [kurari license module documentation](https://www.nag.com/numeric/py/nagdoc_latest/naginterfaces.kusari.html#kusari)

<!-- # References
* Kowalik J S and Osborne, M R (1968) _Methods for unconstrained optimization problems_. New York, American Elsevier Pub. Co
--!>
