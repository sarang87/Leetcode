import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    mx = - sys.maxsize
    mn = sys.maxsize
    mad = mn
    s_arr = sorted(arr)
    print(s_arr)
    j = 0
    for i in range(1,len(s_arr)):
        if abs(s_arr[i]-s_arr[j]) < mad:
            mad = s_arr[i]-s_arr[j]
        i+=1
        j+=1
    return mad

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

