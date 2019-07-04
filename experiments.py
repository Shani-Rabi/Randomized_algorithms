import numpy as np
import perfect_matching as pm
import k_regular as kr
import expander as ex
import clique as cq
import sys
sys.setrecursionlimit(3500)

def print_exp_res(num_of_vertices, exp1, exp2, exp3, exp_av):
    print("number of vertices:")
    print(num_of_vertices)
    print("exp 1 result:")
    print(exp1)
    print("exp 2 result:")
    print(exp2)
    print("exp 3 result:")
    print(exp3)
    print("average:")
    print(exp_av)
    print("-----------------------------------------")

def experiment1():
    print("-------------- Exp 1 : Clique Data --------------")

    clique_num_of_vertices = np.empty(20, dtype=np.object)
    clique_num_of_fails1 = np.empty(20, dtype=np.object)
    clique_num_of_fails2 = np.empty(20, dtype=np.object)
    clique_num_of_fails3 = np.empty(20, dtype=np.object)
    clique_num_of_fails_av = np.empty(20, dtype=np.object)
    for i in range(0, 20):
        curr_n = (i+3)*(i+3) * 6
        graph = cq.create_clique(curr_n)
        clique_num_of_vertices[i] = curr_n
        clique_num_of_fails1[i] = pm.perfect_matching(graph[0], graph[1])[1]
        clique_num_of_fails2[i] = pm.perfect_matching(graph[0], graph[1])[1]
        clique_num_of_fails3[i] = pm.perfect_matching(graph[0], graph[1])[1]
        clique_num_of_fails_av[i] = (clique_num_of_fails1[i] + clique_num_of_fails2[i] + clique_num_of_fails3[i]) / 3
        print("n = "+str(curr_n)+" done")

    print_exp_res(clique_num_of_vertices, clique_num_of_fails1, clique_num_of_fails2,
                  clique_num_of_fails3, clique_num_of_fails_av)

    print("-------------- End Of Exp 1  --------------")



def experiment2():
    print("-------------- Exp 2 : Expander Data --------------")
    print("-------------- Angluin Data --------------")

    angluin_num_of_vertices = np.empty(20, dtype=np.object)
    angluin_num_of_fails1 = np.empty(20, dtype=np.object)
    angluin_num_of_fails2 = np.empty(20, dtype=np.object)
    angluin_num_of_fails3 = np.empty(20, dtype=np.object)
    angluin_num_of_fails_av = np.empty(20, dtype=np.object)
    for i in range(0, 20):
        graph = ex.angluin_method((i + 3) * 2)
        angluin_num_of_vertices[i] = (i + 3) * (i + 3) * 4
        angluin_num_of_fails1[i] = pm.perfect_matching(graph[0], graph[1])[1]
        angluin_num_of_fails2[i] = pm.perfect_matching(graph[0], graph[1])[1]
        angluin_num_of_fails3[i] = pm.perfect_matching(graph[0], graph[1])[1]
        angluin_num_of_fails_av[i] = (angluin_num_of_fails1[i] + angluin_num_of_fails2[i] + angluin_num_of_fails3[
            i]) / 3
        print("Angluin : n = "+str(angluin_num_of_vertices[i])+" done")

    print_exp_res(angluin_num_of_vertices, angluin_num_of_fails1, angluin_num_of_fails2,
                  angluin_num_of_fails3, angluin_num_of_fails_av)

    print("-------------- Margulis Data --------------")

    margulis_num_of_vertices = np.empty(20, dtype=np.object)
    margulis_num_of_fails1 = np.empty(20, dtype=np.object)
    margulis_num_of_fails2 = np.empty(20, dtype=np.object)
    margulis_num_of_fails3 = np.empty(20, dtype=np.object)
    margulis_num_of_fails_av = np.empty(20, dtype=np.object)
    for i in range(0, 20):
        graph = ex.margulis_method((i + 3) * 2)
        margulis_num_of_vertices[i] = (i + 3) * (i + 3) * 4
        margulis_num_of_fails1[i] = pm.perfect_matching(graph[0], graph[1])[1]
        margulis_num_of_fails2[i] = pm.perfect_matching(graph[0], graph[1])[1]
        margulis_num_of_fails3[i] = pm.perfect_matching(graph[0], graph[1])[1]
        margulis_num_of_fails_av[i] = (margulis_num_of_fails1[i] + margulis_num_of_fails2[i] + margulis_num_of_fails3[
            i]) / 3
        print("Margulis : n = "+str(margulis_num_of_vertices[i])+" done")

    print_exp_res(margulis_num_of_vertices, margulis_num_of_fails1, margulis_num_of_fails2,
                  margulis_num_of_fails3, margulis_num_of_fails_av)

    print("-------------- End Of Exp 2  --------------")

def experiment3():
    print("-------------- Exp 3 : comparison with Random graphs --------------")
    print("-------------- 3-Regular Data --------------")
    k_regular_num_of_vertices = np.empty(20, dtype=np.object)
    k_regular_num_of_fails1 = np.empty(20, dtype=np.object)
    k_regular_num_of_fails2 = np.empty(20, dtype=np.object)
    k_regular_num_of_fails3 = np.empty(20, dtype=np.object)
    k_regular_num_of_fails_av = np.empty(20, dtype=np.object)

    for i in range(0, 20):
        curr_n = (i+3)*(i+3) * 4
        graph = kr.get_k_regular(curr_n, 3)
        k_regular_num_of_vertices[i] = curr_n
        k_regular_num_of_fails1[i] = pm.perfect_matching(graph[0], graph[1])[1]
        k_regular_num_of_fails2[i] = pm.perfect_matching(graph[0], graph[1])[1]
        k_regular_num_of_fails3[i] = pm.perfect_matching(graph[0], graph[1])[1]
        k_regular_num_of_fails_av[i] = (k_regular_num_of_fails1[i] + k_regular_num_of_fails2[i] +
                                        k_regular_num_of_fails3[i]) / 3
        print("3 reg : n = "+str(curr_n)+" done")

    print_exp_res(k_regular_num_of_vertices, k_regular_num_of_fails1, k_regular_num_of_fails2,
                  k_regular_num_of_fails3, k_regular_num_of_fails_av)

    print("-------------- 5-Regular Data --------------")
    k_regular_num_of_vertices = np.empty(20, dtype=np.object)
    k_regular_num_of_fails1 = np.empty(20, dtype=np.object)
    k_regular_num_of_fails2 = np.empty(20, dtype=np.object)
    k_regular_num_of_fails3 = np.empty(20, dtype=np.object)
    k_regular_num_of_fails_av = np.empty(20, dtype=np.object)

    for i in range(0, 20):
        curr_n = (i + 3) * (i + 3) * 4
        graph = kr.get_k_regular(curr_n, 5)
        k_regular_num_of_vertices[i] = curr_n
        k_regular_num_of_fails1[i] = pm.perfect_matching(graph[0], graph[1])[1]
        k_regular_num_of_fails2[i] = pm.perfect_matching(graph[0], graph[1])[1]
        k_regular_num_of_fails3[i] = pm.perfect_matching(graph[0], graph[1])[1]
        k_regular_num_of_fails_av[i] = (k_regular_num_of_fails1[i] + k_regular_num_of_fails2[i] +
                                        k_regular_num_of_fails3[i]) / 3
        print("5 reg : n = "+str(curr_n)+" done")

    print_exp_res(k_regular_num_of_vertices, k_regular_num_of_fails1, k_regular_num_of_fails2,
                  k_regular_num_of_fails3, k_regular_num_of_fails_av)

    print("-------------- Clique Data --------------")

    clique_num_of_vertices = np.empty(20, dtype=np.object)
    clique_num_of_fails1 = np.empty(20, dtype=np.object)
    clique_num_of_fails2 = np.empty(20, dtype=np.object)
    clique_num_of_fails3 = np.empty(20, dtype=np.object)
    clique_num_of_fails_av = np.empty(20, dtype=np.object)
    for i in range(0, 20):
        curr_n = (i + 3) * (i + 3) * 4
        graph = cq.create_clique(curr_n)
        clique_num_of_vertices[i] = curr_n
        clique_num_of_fails1[i] = pm.perfect_matching(graph[0], graph[1])[1]
        clique_num_of_fails2[i] = pm.perfect_matching(graph[0], graph[1])[1]
        clique_num_of_fails3[i] = pm.perfect_matching(graph[0], graph[1])[1]
        clique_num_of_fails_av[i] = (clique_num_of_fails1[i] + clique_num_of_fails2[i] + clique_num_of_fails3[i]) / 3
        print("clique : n = "+str(curr_n)+" done")

    print_exp_res(clique_num_of_vertices, clique_num_of_fails1, clique_num_of_fails2,
                  clique_num_of_fails3, clique_num_of_fails_av)

    print("-------------- End Of Exp 3  --------------")

def experiment4():
    print("-------------- Exp 4 : Bollobas method - Random d-Regular --------------")
    d_arr = [2,3,4,5,6]*6
    k_regular_num_of_vertices = [10]*5 + [20]*5 + [50]*5 + [100]*5 + [500]*5 + [1000]*5
    k_regular_num_of_fails1 = np.empty(20, dtype=np.object)
    k_regular_num_of_fails2 = np.empty(20, dtype=np.object)
    k_regular_num_of_fails3 = np.empty(20, dtype=np.object)
    k_regular_num_of_fails_av = np.empty(20, dtype=np.object)

    for i in range(0,20):
        graph = kr.get_k_regular(k_regular_num_of_vertices[i], d_arr[i])
        k_regular_num_of_fails1[i] = pm.perfect_matching(graph[0], graph[1])[1]
        k_regular_num_of_fails2[i] = pm.perfect_matching(graph[0], graph[1])[1]
        k_regular_num_of_fails3[i] = pm.perfect_matching(graph[0], graph[1])[1]
        k_regular_num_of_fails_av[i] = (k_regular_num_of_fails1[i] + k_regular_num_of_fails2[i] +
                                        k_regular_num_of_fails3[i]) / 3
        print("n = " + str(k_regular_num_of_vertices[i]) + " d = " + str(d_arr[i]) + " done")

    print_exp_res(k_regular_num_of_vertices, k_regular_num_of_fails1, k_regular_num_of_fails2,
                  k_regular_num_of_fails3, k_regular_num_of_fails_av)

    print("-------------- End Of Exp 4  --------------")

def experiment5():
    print("-------------- Exp 5 : The direct graphs generations --------------")
    num_of_vertices = np.empty(15, dtype=np.object)
    num_of_fails1 = np.empty(15, dtype=np.object)
    num_of_fails2 = np.empty(15, dtype=np.object)
    num_of_fails3 = np.empty(15, dtype=np.object)
    num_of_fails_av = np.empty(15, dtype=np.object)
    print("-------------- d = n --------------")
    for i in range (0,15):
        num_of_vertices[i] = 4*((i+1)**2)
        graph = cq.create_clique(num_of_vertices[i])
        num_of_fails1[i] = pm.perfect_matching(graph[0], graph[1])[1]
        num_of_fails2[i] = pm.perfect_matching(graph[0], graph[1])[1]
        num_of_fails3[i] = pm.perfect_matching(graph[0], graph[1])[1]
        num_of_fails_av[i] = (num_of_fails1[i] + num_of_fails2[i] + num_of_fails3[i]) / 3
        print("d = n : n = " + str(num_of_vertices[i]) + " done")

    print_exp_res(num_of_vertices, num_of_fails1, num_of_fails2, num_of_fails3, num_of_fails_av)

    print("-------------- d = n/2 --------------")
    for i in range(0, 15):
        graph = kr.get_n2_regular(num_of_vertices[i])
        num_of_fails1[i] = pm.perfect_matching(graph[0], graph[1])[1]
        num_of_fails2[i] = pm.perfect_matching(graph[0], graph[1])[1]
        num_of_fails3[i] = pm.perfect_matching(graph[0], graph[1])[1]
        num_of_fails_av[i] = (num_of_fails1[i] + num_of_fails2[i] + num_of_fails3[i]) / 3
        print("d = n/2 : n = " + str(num_of_vertices[i]) + " done")

    print_exp_res(num_of_vertices, num_of_fails1, num_of_fails2, num_of_fails3, num_of_fails_av)

    print("-------------- d = n/4 --------------")
    for i in range(0, 15):
        graph = kr.get_n4_regular(num_of_vertices[i])
        num_of_fails1[i] = pm.perfect_matching(graph[0], graph[1])[1]
        num_of_fails2[i] = pm.perfect_matching(graph[0], graph[1])[1]
        num_of_fails3[i] = pm.perfect_matching(graph[0], graph[1])[1]
        num_of_fails_av[i] = (num_of_fails1[i] + num_of_fails2[i] + num_of_fails3[i]) / 3
        print("d = n/4 : n = " + str(num_of_vertices[i]) + " done")

    print_exp_res(num_of_vertices, num_of_fails1, num_of_fails2, num_of_fails3, num_of_fails_av)

    print("-------------- End Of Exp 5  --------------")

if __name__ == "__main__":
    exp_num = input("Choose experiment number (1 - 5) to run: ")
    print(exp_num)
    if exp_num == '1':
        experiment1()
    elif exp_num == '2':
        experiment2()
    elif exp_num == '3':
        experiment3()
    elif exp_num == '4':
        experiment4()
    elif exp_num == '5':
        experiment5()
    else:
        print("Invalid number")



