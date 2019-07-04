import numpy as np

def print_graph(v1, v2):
    for i in range(0, len(v1)):
        print(i, end=' ')
        print("->", end=' ')
        for j in range(0, len(v1[i])):
            print(v1[i][j], end=' ')
        print("")

    print("---------------------------------")

    for i in range(0, len(v2)):
        print(i + len(v2), end=' ')
        print("->", end=' ')
        for j in range(0, len(v2[i])):
            print(v2[i][j], end=' ')
        print("")


def print_h(h):
    n = len(h[1][0])
    print("s ->", end=' ')
    print(h[0])

    for i in range (0,n):
        print(i, end=' ')
        print("->", end=' ')
        print(h[1][0][i], end=' ')
        print("in M:", end=' ')
        print(h[1][1][i], end=' ')
        print("")

    for i in range (0,n):
        print(i+n, end=' ')
        print("->", end=' ')
        print(h[2][0][i], end=' ')
        print("in M:", end=' ')
        print(h[2][1][i], end=' ')
        print("")


# G is represented by v1 and v2
# v1 is a list of neighbors
# for example : v1 = [[3,4], [4,3]]
# vertice 0 points at vertices 3 and 4 in v2
# vertice 1 points at vertices 4 and 5 in v2
# v1 contains 2 vertices (len(v1) = n)

# H is an array of 3:
# H[0] - s neighbours
# H[1] -
#        H[1][0] - v1 neighbours: H[1][0][i] - contains the list of neighbours of vertice i
#        H[1][1] - array of mathces: H[1][1][i] - contains -1 if this vertice i is not matched, otherwise
#												  contains the vertice number it matches to  			
# H[2] - H[2][0] - v2 neighbours: H[2][0][i] - contains the list of neigbours of vertice i (might be empty 
#											   if the vertice is matched)												
#        H[2][1] - array of mathces: H[2][1][i] - contains -1 if this vertice i is not matched, otherwise
# 												  contains the vertice number it matches to

									
def transform_g_to_h(v1, v2, m):
    H = np.empty(3, dtype=np.object)
    h1 = np.empty(2, dtype=np.object)
    h2 = np.empty(2, dtype=np.object)
    n = len(v1)
    k = len(v1[0])
    v1_matched = [-1]* n 
    v2_matched = [-1]* n
    s_neighbors = list(range(n)) # at first, s points to all v1 vertices
    t_id = 't'
    h2[0] = [[t_id]*k]*n         # at first, v2 vertices points d times to vertice t

	
	# Matched vertices would be supernodes - we represent it with the array of mathces:
	# 									 	 We add the matched vertices to their partners. 
	# We update s neigbours - should not include matched vertices
	# v2 matched vertices don't have a 	
    for i in range (0, len(m)):
        v1_matched[m[i][0]] = m[i][1]
        v2_matched[m[i][1] - n] = m[i][0]
        s_neighbors.remove(m[i][0])
        h2[0][m[i][1]-n] = []

    s_neighbors = s_neighbors * k # s points to each unmatched vertice d times
    s_neighbors.sort()
    h1[0] = v1
    h1[1] = v1_matched
    h2[1] = v2_matched

    H[0] = s_neighbors
    H[1] = h1
    H[2] = h2

    return H

	
# returns a uniformly random neigbour of u	
def sample_out_edge(H,u):
    n = len(H[1][0])
    if(u == 's'):
        v_index = np.random.randint(0, len(H[0]))
        return H[0][v_index]

    if(u >= n): # u belong to v2. It doesn't have a match because we checked it first in truncated_walk
        return 't'
		
		
	# u belong to v1
    v_index = np.random.randint(0, len(H[1][0][u]))
    return H[1][0][u][v_index]

# path must be [] at first
def truncated_walk(H,u,b,path):
    n = len(H[1][0])
    if(u == 's'):
        b = b - 1
        if(b<0):
            return  False
        u = sample_out_edge(H,u)

    for i in range(0,int(b)):
        if(u == 't'):
            return path

        if(u >= n):
            u_match = H[2][1][u - n]
            if (u_match != -1):  # u is a part of a super node - it doesn't have neigbours of its own,
                # only the neigbours of its matched vertice
                path.append(u)
                u = u_match
        path.append(u)
        u = sample_out_edge(H,u)

    return False

def check_for_circles_and_remove(path):
    for i in range(0, len(path)):
        for j in range((i+1), len(path)):
            if(path[i] == path[j]):
                del path[i:j]
                return path
    return -1

# going over the match, if the path and match share an edge - we remove it. else we add it
def symmetric_difference(match,path):
    for i in range (0, len(match)):
        if(match[i] in path):
            path.remove(match[i])
        else:
            if ([match[i][1], match[i][0]] in path):
                path.remove([match[i][1], match[i][0]])
            else:
                path.append(match[i])
    return path

def get_match_from_path(match, path):
    res = check_for_circles_and_remove(path)

    while(res != -1):
        path = res
        res = check_for_circles_and_remove(path)

    fixed_path = []
    i = 0
    while(i < len(path)-1): ## append edges to the fixed_path (for example the path [0,1,2,3] turns to [ [0,1][2,3] ] )
        fixed_path.append([path[i], path[i+1]])
        i = i+1

    return symmetric_difference(match,fixed_path)

def get_b(n,j):
    return 2*(2+(n/(n-j)))

def perfect_matching(v1,v2):
    # 1 - set j = 0, m0 = []
    num_of_iters = 0
    j = 0
    m = []
    n = len(v1)

    while(len(m) < n): # run the algorithm till you have perfect matching of size n

        # 2 - get the new path from the graph H (defined by the current match)
        h = transform_g_to_h(v1, v2, m)
        b = get_b(n,j)
        path = truncated_walk(h,'s',b,[])
        #num_of_iters = num_of_iters+1
        while(path == False):
            num_of_iters = num_of_iters + 1
            path = truncated_walk(h, 's', b, [])

        # 3 - Set the new match: match := match∆path.
        m = get_match_from_path(m,path)

        j = j+1

    return [m, num_of_iters]

if __name__ == "__main__":
    print("algorithm")