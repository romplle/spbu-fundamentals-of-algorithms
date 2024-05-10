import numpy as np


def cholesky(A):
    n = len(A)
    L = np.zeros_like(A, dtype=np.float64)

    for i in range(n):
        for j in range(i+1):
            if j == i:
                L[i, j] = np.sqrt(A[i, i] - np.sum(L[i, :j]**2))
            else:
                L[i, j] = (A[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j]
    return L


if __name__ == "__main__":
    L = np.array(
        [
            [1.0, 0.0, 0.0],
            [4.0, 2.0, 0.0],
            [6.0, 5.0, 3.0],
        ]
    )

    A = L @ L.T
    print("Original Matrix A:")
    print(A)

    L_new = cholesky(A)
    print("\nCholesky L:")
    print(L_new)

    A_new = L_new @ L_new.T
    print("\nNew Matrix A:")
    print(A_new)