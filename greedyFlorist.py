#!/bin/python3
# https://www.hackerrank.com/challenges/greedy-florist/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms&isFullScreen=true
import math
import os
import random
import re
import sys


def helper(arr, k, pr):  
    l = len(arr)
    if l == 0:
        return 0
    if k >= len(arr):
        print ("arr:{}, pr:{}".format(arr, pr))      
        print ("cost:{}".format(sum(arr)))
        return sum(arr) * (pr+1)
    else:
        cost = sum(arr[l-k:]) * (pr+1) + helper(arr[0:l-k],k,pr+1)
        print ("rec_cost:{}".format(cost))
        return cost
        
    
# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    c = sorted (c)
    l = len(c)
    if k >= len(c):     
        return sum(c)
    else:
        s = sum(c[l-k:])
        print(s)
        cost =  s + helper(c[0:l-k],k,1)
        return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
