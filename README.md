## Jacobson-Truax-Plot

[!img sample_data_masked.png]

A simple Python script for visualizing the outcome of **Jacobson-Truax's method** for calculating clinical significance scores ([1](https://en.wikipedia.org/wiki/Clinical_significance#Jacobson-Truax)).

### How to use
Data must be organized in an Excel spreadsheet - use the sample data file as a reference on how to do this. You simply need to copy-paste your own data into it.

Some parameters can be customized by changing values in the `SETTINGS` dictionary at the top of the `JT_plot.py` file.

### Dependencies
Use **Python >= 3.7** to run this script.

This script depends on the following Python packages:
- Pandas
- Matplotlib

This repository also includes the Seaborn Scattermap-Dotplot snippet from [@lukauskas](https://github.com/lukauskas) - [source available here](https://gist.github.com/lukauskas/f2f43aad6078a8b5d71b986174487b8c).

### License
This script is distributed under the MIT license - read the `LICENSE.md` file for more information.
