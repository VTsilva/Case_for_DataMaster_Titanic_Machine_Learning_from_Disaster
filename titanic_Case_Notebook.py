#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%%
test_path = "./data/test.csv"
train_path = "./data/train.csv"
test_df = pd.read_csv(test_path)
train_df = pd.read_csv(train_path)
#%%
display(test_df)

#%%
display(train_df)
# %%
