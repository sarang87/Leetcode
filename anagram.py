#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    d = {}
    s=""
    for i in a:
        print(i)
        if i in d:
            c = d[i]
            d[i] = c+1
        else:
            d[i] = 1
    print (d)
    for j in b:
        if j in d:
            n = d[j]
            s+=j
            if n == 1:
                del(d[j])
            else:
                d[j] == n-1
        else:

    
    print(s)
    return len(a) + len(b) - (2 *len(s))
        

if __name__ == '__main__':

    a = 'fcrxzwscanmligyxyvym'

    b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

    res = makeAnagram(a, b)




