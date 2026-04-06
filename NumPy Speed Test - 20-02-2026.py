# NumPy Speed Test

import time
import numpy as np

# Creating 1 million numbers
python_list = list(range(1, 1000001))
numpy_array = np.arange(1, 1000001)

# Python List Operation

start_time = time.time()

python_result = [x * 2 for x in python_list]

end_time = time.time()
python_time = end_time - start_time

# NumPy Array Operation

start_time = time.time()

numpy_result = numpy_array * 2

end_time = time.time()
numpy_time = end_time - start_time

# Display Results

print("----- Execution Time Comparison -----")
print(f"Python List Time: {python_time:.6f} seconds")
print(f"NumPy Array Time: {numpy_time:.6f} seconds")


# Compare which is faster

if python_time > numpy_time:
    print("\nNumPy is faster than Python List.")
else:
    print("\nPython List is faster than NumPy (rare case).")



# The 3 Observations are :-

# Observation 1
# -NumPy arrays are much faster than Python lists for numerical operations on large datasets.

# Observation 2
# -Python lists require element-by-element processing, while NumPy performs vectorized operations, which are highly optimized.

# Observation 3
# -NumPy is more suitable for data science, machine learning, and scientific computing because it handles large numerical data efficiently.