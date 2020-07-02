### Building the static pages from these notebooks

These notebook uses the `latex_envs` Jupyter extension at https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/latex_envs/README.html and attempting to produce the pdf version from the Jupyter GUI did not work. Instead, The pdf output was produced from the notebook using the following command after the `latex_envs` extension was installed.

```
jupyter nbconvert --to pdf portfolio_optimization_using_socp.ipynb
jupyter nbconvert --to html_with_lenvs portfolio_optimization_using_socp.ipynb
```
