# Main script: Compare NumPy vs Python Lists
import numpy as np
import time
from custom_math import operations # may fail: check PYTHONPATH!

size = 1_000_000

# NumPy array
np_arr = np.random.rand(size)
start = time.time()
np_sum = np_arr.sum()
np_arr.sort()
print(f"NumPy Time: {time.time() - start:.5f} sec")

# Python list
py_list = list(np.random.rand(size))
start = time.time()
py_sum = operations.list_sum(py_list)
py_sorted = operations.list_sort(py_list)
print(f"Python List Time: {time.time() - start:.5f} sec")
