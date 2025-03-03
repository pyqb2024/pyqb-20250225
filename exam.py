# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.6
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Programming in Python
# ## Exam: February 25, 2025
#
#
# You can solve the exercises below by using standard Python 3.12 libraries, NumPy, Matplotlib, Pandas, PyMC.
# You can browse the documentation: [Python](https://docs.python.org/3.12/), [NumPy](https://numpy.org/doc/1.26/index.html), [Matplotlib](https://matplotlib.org/3.10.0/users/index.html), [Pandas](https://pandas.pydata.org/pandas-docs/version/2.2/index.html), [PyMC](https://www.pymc.io/projects/docs/en/stable/api.html).
# You can also look at the [slides](https://homes.di.unimi.it/monga/lucidi2425/pyqb00.pdf) or your code on [GitHub](https://github.com).
#
#
# **The exam is "open book", but it is strictly forbidden to communicate with others or "ask questions" online (i.e., stackoverflow is ok if the answer is already there, but you cannot ask a new question or use ChatGPT and similar products). Suspicious canned answers or plagiarism among student solutions will cause the invalidation of the exam for all the people involved.**
#
# To test examples in docstrings use
#
# ```python
# import doctest
# doctest.testmod()
# ```

# **SOLVE EACH EXERCISE IN ONE OR MORE NOTEBOOK CELLS AFTER THE QUESTION.**

import numpy as np   # type: ignore
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt # type: ignore
import pymc as pm   # type: ignore

# ### Exercise 1 (max 1 points)
#
# The file [Howell1.csv](./Howell1.csv) contains partial census data for !Kung San people (Africa), collected by Nancy Howell (~ 1960), csv comes from R. McElreath, "Statistical Rethinking", 2020.
#
# Read the file in a proper Pandas DataFrame.
#
#

pass

# ### Exercise 2 (max 6 points)
#
# We want to add to data a new column `parent` with the index number of one the parents of the individual described by the current row. For example, if the row with index 3 has 0 has its `parent`, this means that the individual described by the row with index 0 is one of the parents of the individual described by row with index 3. 
# The `parent` column must be populated by randomly selecting from all individuals with an age greater than the child's age plus 15
# years, but less then the child's age plus 50. To illustrate this, for the male individual in the row 3 (aged 41), any of the 66 individuals aged between 56 and 91 (extremes included) could be chosen as a parent. In the random selection process, each potential candidate should have an equal probability of being selected. If no individual old enough exists, the parent should be set to -1.

pass

# ### Exercise 3 (max 5 points)
#
# Compute the average age difference between an individual and their parent (ignore -1 parents). To get the full marks do not use explicit loops.

pass

# ### Exercise 4 (max 6 points)
#
# Define a function that takes a Pandas Series and compute a new Series in which each pair of consecutive values is swapped. For example, if the values are 1,2,3,4,5 then the result is a Series with 2,1,4,3,5.
#
# To get the full marks, you should declare correctly the type hints and add a doctest string.

pass

# ### Exercise 5 (max 3 points)
#
# Make a scatter plot with the age of each individual and the age of their parent (ignore -1 parents). Put proper labels on the axis.

pass

# ### Exercise 6 (max 4 points)
#
# Consider only the individuals with a parent of the same sex. On the same axis, make a picture with two scatter plots with different colors, one per sex, of the height of the parent and the height of the child. Put proper labels and a legend.

pass

# ### Exercise 7 (max 4 points)
#
# Add a column `siblings` with the number of child with the same parent as the current individual (consider individual with a -1 parent as siblings). To get the full marks do not use explicit loops.

pass

# ### Exercise 8 (max 4 points)
#
# Consider this statistical model: the height of individual with a parent (different from -1) is normal with an unknown mean $\alpha + \beta\cdot H_p$, where $H_p$ is the height of the parent, and an unknown standard deviation $\sigma$. Your *a priori* estimation for both $\alpha$ and $\beta$ distribution is a normal distibution with mean 0 and std deviation 5; your *a priori* estimation for $\sigma$ exponential distribution with $\lambda=1$. Use PyMC to sample the posterior distributions after having seen the actual values for the heights. Plot the posterior distributions of the variables.

pass
