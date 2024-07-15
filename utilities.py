# Databricks notebook source
import numpy as np
from matplotlib import pyplot as plt

# COMMAND ----------

x = np.random.normal(0, 1, 10000)
plt.hist(x, bins=50)
