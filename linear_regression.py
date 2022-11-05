from sklearn.datasets import load_boston
#house pricing dataset
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=load_boston()
dataset=pd.DataFrame(df.data)
dataset.columns=df.features_names
print(dataset.head())

