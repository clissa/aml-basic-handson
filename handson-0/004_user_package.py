# Main script: Compare NumPy vs Python Lists
import numpy as np
import time
from pathlib import Path
from custom_math import operations # may fail: check PYTHONPATH!

# # FIX: Add custom_math to PYTHONPATH if not already present
# import sys
# sys.path

# module_dir = Path(".").resolve() / "handson-0"
# if str(module_dir) not in sys.path:
# 	sys.path.insert(0, str(module_dir))
# try:
# 	from custom_math import operations
# except ImportError as e:
	# print(f"Error: Could not import custom_math module. {e}")
# 	print(f"Module directory: {module_dir}")
# 	print(f"PYTHONPATH: {sys.path}")
# 	sys.exit(1)
	
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
