# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
#!/bin/python3

import math
import os
import random
import re
import sys

def find(s1, s2):
    p =0
    q=0
    l1 = len(s1)
    l2 = len(s2)
    l = min(l1,l2)
    i = 0
    s = ""
    while i < l:
        if s1[p] == s2[q]:
            s+=s1[p]
        else:
            print("ss:{}".format(s))
            return s       
        i+=1

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    
    d = {}
    for ix, i in enumerate(s1):
        if i in d:
            l = d[i]
            l.append(ix)
        else:
            ll = []
            ll.append(ix)
            d[i] = ll
    print(d)
        
    res = []
    for idx,c in enumerate(s2):
        if c in d:
            l = d[c]
            for six in l:
                ss = find (s1[six:],s2[idx:])
                if ss != "":
                    res.append(ss) 
                    return "YES"
                
                         
        else:
            continue
    #     if c == s2[ptr]:
    #         find()
    print(res)
    if len(res) > 0:
        print("YES")
        return "YES"
    else:
        print("NO")
        return "NO"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()