import numpy as np
import perfect_matching as pm

def angluin_method(n):
    if(n < 2):
        return -1
    v_num = n*n
    a = list(range(n))
    b = list(range(n))
    v1 = np.empty(v_num, dtype=np.object)
    v2 = np.empty(v_num, dtype=np.object)
    for i in range (0,v_num):
        v2[i] = []

    vertices = [[a0, b0] for a0 in a for b0 in b]

    for i in range(0, len(vertices)):
        x = vertices[i][0]
        y = vertices[i][1]
        i1 = vertices.index([x,y])
        i2 = vertices.index([((x+y)%n), y])
        i3 = vertices.index([((y+1)%n), ((-x)%n)])
        v1[i] = [i1+v_num, i2+v_num, i3+v_num]
        v2[i1].append(i)
        v2[i2].append(i)
        v2[i3].append(i)

    #pm.print_graph(v1,v2)

    return [v1, v2]

def margulis_method(n):
    if(n < 3):
        return -1
    v_num = n*n
    a = list(range(n))
    b = list(range(n))
    v1 = np.empty(v_num, dtype=np.object)
    v2 = np.empty(v_num, dtype=np.object)
    for i in range (0,v_num):
        v2[i] = []

    vertices = [[a0, b0] for a0 in a for b0 in b]

    for i in range(0, len(vertices)):
        x = vertices[i][0]
        y = vertices[i][1]
        i1 = vertices.index([x,y])
        i2 = vertices.index([x,(y+1)%n])
        i3 = vertices.index([(x+1)%n,y])
        i4 = vertices.index([(x+y)%n,y])
        i5 = vertices.index([(-y)%n,x])
        v1[i] = [i1+v_num, i2+v_num, i3+v_num, i4+v_num, i5+v_num]
        v2[i1].append(i)
        v2[i2].append(i)
        v2[i3].append(i)
        v2[i4].append(i)
        v2[i5].append(i)

    #pm.print_graph(v1,v2)

    return [v1, v2]


if __name__ == "__main__":
    print("expander")
