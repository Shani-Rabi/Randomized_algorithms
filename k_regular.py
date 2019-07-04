import numpy as np
import perfect_matching as pm

def print_array(arr):
    print("----------------------------")
    for i in range(0 , len(arr)):
        print(arr[i])
    print("----------------------------")

def create_k_regular_random_graphs(n,k):
    V1 = np.empty(n, dtype=np.object)
    V2 = np.empty(n, dtype=np.object)
    V2_vertices_to_choose = [0]*n*k  
    index = 0;

    for i in range (0 , n):
        for j in range (0, k):
            V2_vertices_to_choose[index] = i+n 
            index = index + 1

    for i in range(0, n):
        V1[i] = []
        V2[i] = []

	# nk times we randomly choose another vertex 	
    for i in range(0, n):
        for j in range(0, k):
            index_vertice_to_pair = np.random.randint(0, len(V2_vertices_to_choose))
            ver_num = V2_vertices_to_choose[index_vertice_to_pair]
            if ver_num in V1[i]:
                return False
            V1[i].append(ver_num)
            V2[ver_num-n].append(i)
            V2_vertices_to_choose.pop(index_vertice_to_pair)
    #print("success")
    #pm.print_graph(V1, V2) #TODO : REMOVE
    return [V1, V2]

def get_k_regular(n, k):
    while(True):
        g = create_k_regular_random_graphs(n,k)
        if(g != False):
            return g

def get_n2_regular(n):
    v1 = np.empty(n, dtype=np.object)
    v2 = np.empty(n, dtype=np.object)

    even1 = []
    even2 = []
    odd1 = []
    odd2 = []

    for i in range (0,n):
        if(i%2 == 0):
            even1.append(i+n)
            even2.append(i)
        else:
            odd1.append(i+n)
            odd2.append(i)

    for i in range(0,n):
        if(i%2 == 0):
            v1[i] = even1
            v2[i] = even2
        else:
            v1[i] = odd1
            v2[i] = odd2

    return [v1,v2]


def get_n4_regular(n):
    v1 = np.empty(n, dtype=np.object)
    v2 = np.empty(n, dtype=np.object)

    for i in range(0,n):
        v1[i] = []
        v2[i] = []

    for i in range(0,n):
        for j in range(0,n):
            if((j+n)%4 == i%4):
                v1[i].append(j+n)
                v2[j].append(i)

    return [v1,v2]





if __name__ == "__main__":
    print("k_regular")




