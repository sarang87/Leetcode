#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the isValid function below.
def isValid(s):
    a = collections.Counter(s)
    m = a.most_common()
    print(m)
    l = len(m)
    b = m[0][1]
    b = int(b)
    s = m[l-1][1]
    s = int(s)
    cnt = 0
    h = 0
    p = 0 # b for biggest, u for unique

    # case "mmmmnnnaaar" or case "mmnnaabc"
    if b - s > 1 and b != m[l-2][1]:
        print("NOO")
        return "NO"
    # case "mmmmmmmm" or case "mmnnnrrccdd"
    elif b -s == 0:
        return "YES"
    # all other cases
    else:
        for x in m: 
            #c for current   
            c = int(x[1])     
            if b == c:
                h+=1
                continue
            else:  
                cnt +=1  
                print("{}".format(cnt)) 
                # "hhhhhcc" or "rrrrrcccccdd"     
                if h > 1 and cnt > 1:
                    return "NO"
                
    return "YES"

if __name__ == '__main__':
    
    s = input()

    result = isValid(s)

