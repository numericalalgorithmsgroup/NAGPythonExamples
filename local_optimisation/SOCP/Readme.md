## Portfolio Optimisation using Second Order Cone Programming (SOCP)

Second Order Cone Programming (SOCP) functionality was released at Mark 27 of the NAG library and this folder contains a demonstration of how to perform portfolio optimisation using it.

* [portfolio_optimisation_using_socp.ipynb](./portfolio_optimisation_using_socp.ipynb) - Jupyter notebook
* [portfolio_optimisation_using_socp.html](./portfolio_optimisation_using_socp.html) - Static HTML version

### Building the HTML version

The notebook uses the `latex_envs` Jupyter extension at https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/latex_envs/README.html and attempting to produce the HTML version from the Jupyter GUI did not work. Instead, The HTML output was produced from the notebook using the following command after the `latex_envs` extension was installed.

```
jupyter nbconvert --to html_with_lenvs portfolio_optimisation_using_socp.ipynb
```


