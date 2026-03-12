import math
print(math.sqrt(25))  # 5.0

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr.mean())  # 3.0

import pandas as pd
df = pd.DataFrame({"Name": ["Alice", "Bob"], "Age": [25, 30]})
print(df.head())  

import matplotlib.pyplot as plt
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()
# >>> plt.show()
# <stdin>:1: UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown
# This happens if matplotlib is using a non-GUI backend (Agg, default), thus it cannot open a window with the plot. This often happens in WSL without GUI support.
# To fix this, you can either:
# 1. Use a different backend that supports GUI (e.g., TkAgg, QtAgg) by adding the following lines before importing matplotlib:
#    import matplotlib
#    matplotlib.use('TkAgg')  # or 'QtAgg'
# 2. Use a Jupyter Notebook or JupyterLab environment, which can display plots inline without needing a GUI backend.
# Note: If you are using WSL and want to display plots, you may need to set up an X server on Windows (e.g., Xming) and configure WSL to use it. Alternatively, consider using a Jupyter Notebook for a more seamless experience.
# 3. Install a GUI backend in WSL (e.g., $sudo apt install python3-tk)
# Note: after installing GUI backend, tkagg becomes matplotlib's default backend, so you don't need to set it explicitly.
# >>> import matplotlib
# >>> print(matplotlib.get_backend())