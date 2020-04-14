from subprocess import run, PIPE
import random
import math
from utils import MachinesIPs, NODES_NUMBER
if __name__ == "__main__":
    runFileName = "main.py"
    groups = []
    k = int(math.sqrt(NODES_NUMBER))
    for i in range(k):
        groups.append([])
    i = 0
    j = 0
    end = 0
    while (end < NODES_NUMBER):
        groups[i].append((i, j))
        i = (i + 1) % k
        if(i == 0):
            j += 1
        end += 1
    i = 0
    for group in groups:
        for node in group:
            if(node[0] == 2 and node[1] == 2):
                cmd = "python {} {} {} {} {}".format(
                    runFileName, node[0], node[1], MachinesIPs[i], 1)
            else:
                cmd = "python {} {} {} {} {}".format(
                    runFileName, node[0], node[1], MachinesIPs[i], 0)
            #p = run(cmd, shell=True, timeout= 5*60)
            p = run(cmd, shell=True)
            print("Node ({},{}) is created with ip address = {}".format(
                node[0], node[1], MachinesIPs[i]))
            i += 1
