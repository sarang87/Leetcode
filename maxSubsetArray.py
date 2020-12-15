#!/bin/python3
# https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming
import math
import os
import random
import re
import sys

dd = {}

def f(arr,d):
    if len(arr) == 0 or arr is None:
        return -sys.maxsize
    if len(arr) == 1:
        return arr[0]
    # for caching the recursion create a string from the list and store it in a dict as key and the maxSubset Array value as val
    ss1 = str(arr[2:])
    #print("ss1:{}, t:{}".format(ss1, type(ss1)))
    ss2 = str(arr[3:])
    # check dict before recursion
    if ss1 not in dd:   
        p = f(arr[2:],d+1)
        dd[ss1] = p
    else:
        p = dd[ss1]
    if str(arr[3:]) not in dd:
        q = f(arr[3:],d+1)
        dd[ss2] = q
    else:
        q = dd[ss2]      
    s1 = sum(arr[2:])
    s2 = sum(arr[3:])
    a = max(arr[0] + p ,p,s1, arr[0] + s1)
    #print("/t*{},a={}".format(d,a))
    b = max (arr[1] + q,q,s2, arr[1] + s2)
    #print("/t*{},b={}".format(d,b))
    return max (a,b)
    

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    if len(arr) == 0 or arr is None:
        return -sys.maxsize
    if len(arr) == 1:   
        return arr[0] 
    xx = f(arr[2:],0)
    yy = f(arr[3:],0)
    a = max(arr[0] + xx,xx)
    #print("I:{}".format(a))
    b = max (arr[1] + yy,yy)
    #print("II:{}".format(b))
    return max (a,b)
    
# Complete the maxSubsetSum function below.
def maxSubsetSumOptimized(arr):
    dp = {} # key : max index of subarray, value = sum
    dp[0], dp[1] = arr[0], max(arr[0], arr[1])
    for i, num in enumerate(arr[2:], start=2):
        dp[i] = max(dp[i-1], dp[i-2]+num, dp[i-2], num)
    return dp[len(arr)-1]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)