import numpy as np
import perfect_matching as pm

def create_clique(n):
    v1 = np.empty(n, dtype=np.object)
    v2 = np.empty(n, dtype=np.object)
    v1_indexes = list(range(n))
    v2_indexes = list(range(n, n+n))

    for i in range (0, n):
        v1[i] = v2_indexes
        v2[i] = v1_indexes

    #pm.print_graph(v1, v2)
    return [v1,v2]


if __name__ == "__main__":
    print("clique")