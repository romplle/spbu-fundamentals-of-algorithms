import numpy as np
import matplotlib.pyplot as plt

from src.common import NDArrayFloat


def inverse_power_method(A: NDArrayFloat, n_iters: int) -> float:
    n = A.shape[0]
    eigenvector = np.random.rand(n)
    A_inverse = np.linalg.inv(A)
    for i in range(n_iters):
        eigenvector = np.dot(A_inverse, eigenvector)
        eigenvalue = max(abs(eigenvector))
        eigenvector = eigenvector / eigenvalue
    return 1 / (eigenvalue + 1e-10)

if __name__ == "__main__":
    A = np.array(
        [
            [4.0, 1.0, -1.0, 2.0],
            [1.0, 4.0, 1.0, -1.0],
            [-1.0, 1.0, 4.0, 1.0],
            [2.0, -1.0, 1.0, 1.0],
        ]
    )

    n_iters = 100
    smallest_eigenvalue = inverse_power_method(A, n_iters)
    print("Smallest eigenvalue:", smallest_eigenvalue)
