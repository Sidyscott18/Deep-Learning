import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "X": [2, 4, 6, 8, 10],
    "Y": [1, 3, 4, 7, 9]
}

df = pd.DataFrame(data)

cov_matrix = df.cov()
print(cov_matrix)

eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:", eigenvectors)

plt.figure(figsize=(6, 4))
plt.scatter(df["X"], df["Y"])
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot of X and Y")
plt.grid(True)
plt.show()

plt.figure(figsize=(6, 4))
plt.bar(["Eigenvalue 1", "Eigenvalue 2"], eigenvalues)
plt.xlabel("Eigenvalues")
plt.ylabel("Magnitude")
plt.title("Eigenvalue Analysis")
plt.show()
