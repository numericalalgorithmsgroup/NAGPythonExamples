## Portfolio Optimisation using Second Order Cone Programming (SOCP)

Second Order Cone Programming (SOCP) functionality was released at Mark 27 of the NAG library and this folder contains a demonstration of how to perform portfolio optimisation using it.

* [portfolio_optimisation_using_socp.ipynb](./portfolio_optimisation_using_socp.ipynb) - Jupyter notebook
* [portfolio_optimisation_using_socp.pdf](./pdf/portfolio_optimisation_using_socp.pdf) - Static pdf version

### Building the pdf version

The notebook uses the `latex_envs` Jupyter extension at https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/latex_envs/README.html and attempting to produce the pdf version from the Jupyter GUI did not work. Instead, The pdf output was produced from the notebook using the following command after the `latex_envs` extension was installed.

```
jupyter nbconvert --to pdf portfolio_optimisation_using_socp.ipynb
```


