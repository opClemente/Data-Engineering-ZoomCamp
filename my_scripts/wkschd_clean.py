# %% 
# imports1
import pandas as pd
import numpy as np

# %% 
#open file
file = "6.2 Schedules.xlsx"
df = pd.read_excel(
    file,
    skiprows=0,
    header = 0, #row
    nrows=20,
    usecols="A:I" #columns a-i
)
#%%
#drop empty rows
df = df.dropna(axis = 0,
               how = "all")
print(df.head().to_string())
print(df.shape)
print(df.columns)

# %%
#normalize
time_cols = df.columns[2:]
df[time_cols] = df[time_cols].replace(
    r"(\d{1,2})(?::00)?(am|pm)",
    r"\1:00\2",
    regex=True
)
print(df.to_string())

# %%

df.to_excel("schedule_6.2.xlsx", index=False)
 