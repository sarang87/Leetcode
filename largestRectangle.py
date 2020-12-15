#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.

def expand(ix,arr,l):
    ll = ix -1
    hh = ix + 1
    c = arr[ix]
    s = c
    while ll >= 0:
        x = arr[ll]
        if c <= x:
            s+= c
        else:
            break  
        ll-=1     
    while hh < l:
        y = arr[hh]
        if c <= y:
            s+= c
        else:
            break 
        hh+=1
    return s
            
def largestRectangle(h):
    mx = 0
    print(h)
    l = len(h)
    for ix,i in enumerate(h):
        s = expand(ix,h,l)
        print('s:{}'.format(s))
        if s > mx:
            #print('mx:{}'.format(mx))
            mx = s
    print (mx)
    return mx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()