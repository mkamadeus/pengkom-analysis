# %%
import pandas as pd
from IPython.display import display, HTML

#%%
dataframes = []
for i in range(0,15):
    tmp = pd.read_csv('data/fti_'+chr(97+i)+'.csv')
    display(HTML(tmp.to_html()))
    dataframes.append(tmp)


# %%
