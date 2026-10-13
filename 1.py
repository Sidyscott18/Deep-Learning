import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([2, 4, 6])
v2 = np.array([1, 3, 5])

print("Vector Addition:", v1 + v2)
print("Vector Subtraction:", v1 - v2)
print("Dot Product:", np.dot(v1, v2))
print("Scalar Multiplication:", 2 * v1)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix Addition:\n", A + B)
print("Matrix Subtraction:\n", A - B)
print("Matrix Multiplication:\n", np.dot(A, B))
print("Transpose of A:\n", A.T)

plt.bar(range(len(v1)), v1)
plt.title("Vector Elements")
plt.xlabel("Index")
plt.ylabel("Value")

plt.show()
