# A Python library is a collection of pre-written code that helps us
#  perform tasks easily without writing everything from scratch.
# # For example, NumPy is used for numerical calculations, 
# Pandas is used for data handling, and Matplotlib is used for graphs.

# NumPy (Numerical Python) is a library used to perform mathematical operations and work with arrays.

# 1)operations 
import numpy as np

a = np.array([10, 20, 30, 40])

print(a)
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))

# 2)1 D numpy array
import numpy as np

a = np.array([10, 20, 30, 40])
print(a)

# 3)2d array creation
import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a)

# 4)max min operations
import numpy as np

a = np.array([15, 5, 25, 10])

print("Maximum:", np.max(a))
print("Minimum:", np.min(a))

# 5)arithimatic operations on 2D array
import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

# 6)Transpose of 2D array
import numpy as np

a = np.array([[1, 2], [3, 4]])

print(a.T)