import math
import time

import numpy as np



def slow_pairwise_distances(matrix):
    """Very slow, buggy implementation of pairwise distances.

    matrix: list of lists, shape (n_samples, n_features)
    returns: list of lists, shape (n_samples, n_samples)
    """
    #stop index error with if, when no rows
    n_rows = len(matrix)
    if n_rows == 0:
        return []
    n_cols = len(matrix[0])

    def fast_pairwise_distances(matrix):
    """Fpairwise distances using NumPy that is fast, found using google search "optimize pairwise distance using numPy""""
   
    X = np.array(matrix, dtype=float)        
    
    diffs = X[:, None, :] - X[None, :, :]
    
    dists = np.sqrt(np.sum(diffs ** 2, axis=-1))
    return dists.tolist()

    # BUGS: lots of nested loops, some indices are wrong,
    # and computation is inefficient.
    distances = [[0.0 for _ in range(n_cols)] for _ in range(n_rows)]
    for i in range(n_rows):
        for j in range(n_rows):  # BUG: should not loop over n_cols here
            total = 0.0
            for k in range(n_rows):
                diff = matrix[k][j] - matrix[j][k]  # BUG: j indexing
                total += diff * diff
            distances[i][j] = math.sqrt(total)
    return distances

def demo():
    data = [
        [0.0, 0.0],
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 1.0],
    ]

    t0 = time.time()
    dists = slow_pairwise_distances(data)
    t1 = time.time()

    print("Slow distances:")
    for row in dists:
        print(row)
    print(f"Time taken (slow): {t1 - t0:.6f} seconds")

    # TODO: implement and call your optimized version here.

if __name__ == "__main__":
    demo()
