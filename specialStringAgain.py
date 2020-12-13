#!/bin/python3
# Special string again
# https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
import math
import os
import random
import re
import sys

def expand(s,ix):
    l = len (s)
    h = l -ix 
    b = ix - 0
    #print("*** ix:{}, h:{}, b:{} *** ".format(ix,h,b))
    it = min(h,b)
    cnt = 0
    i = ix - 1
    j = ix + 1
    res = []
    while cnt < it:
        #print("it:{}, s[ix]:{}, ix:{}".format(it,s[ix],ix))
        if i >=0 and j <= l-1:
            if s[i] == s[j]:
                if len(res) == 0:
                    adds = s[i:j+1]
                    #print("Adding:{}".format(adds))
                    res.append(adds)
                    i-=1
                    j+=1
                else:
                    if s[i+1] == s[i]:
                        adds = s[i:j+1]
                        #print("Adding:{}".format(adds))
                        res.append(adds)
                        i-=1
                        j+=1
        else:
            #print("\n")
            return res
        cnt+=1
    #print("\n")
    return res
    
def expandeven(s,ix):
    l = len (s)
    h = l -ix 
    b = ix - 0
    it = min(h,b)
    # print("*** ix:{}, h:{}, b:{}, it ={}, s[i] ={} *** ".format(ix,h,b, it, s[ix]))
    cnt = 0
    i = ix
    j = ix + 1
    res = []
    while cnt < it:
        if i >= 0 and j <= l-1:
            if s[i] == s[j]:
                if len(res) == 0:
                    res.append(s[i:j+1])
                    # print("ss={}".format(s[i:j+1]))
                    i-=1
                    j+=1
                if s[i] == s[i+1] and len(res) > 0:
                    # print("ss*={}".format(s[i:j+1]))
                    res.append(s[i:j+1])
                    i-=1
                    j+=1
            else:
                return res
        cnt+=1       
    return res
                    
                        
# Complete the substrCount function below.
def substrCount(n, s):
    d = {}
    rr = []
    for ix,c in enumerate(s):
        rr.append(c)
        res = expand (s, ix)    
        res2 = expandeven (s, ix)
        rr = rr+res2+res
    rcnt = len(rr)
    return rcnt
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()


***************** Merged version

#!/bin/python3

import math
import os
import random
import re
import sys

def expand(s,ix):
    l = len (s)
    #print("*** ix:{}, h:{}, b:{} *** ".format(ix,h,b))
    cnt = 0
    i = ix - 1
    j = ix + 1
    jj = ix + 1
    m = ix
    res = []
    res2 = []
    flag1 = True
    while (i >=0 and j <=l-1) or (m >= 0 and jj <= l-1):
        #print("it:{}, s[ix]:{}, ix:{}".format(it,s[ix],ix))
        if s[i] == s[j] and i >= 0 and j <= l-1:
            if len(res) == 0:
                adds = s[i:j+1]
                print("s[j]:{}, s[i]:{}, ix:{}".format(j,i,ix))
                print("Adding:{}".format(adds))
                res.append(adds)        
            else:
                if s[i+1] == s[i]:
                    adds = s[i:j+1]
                    print("Adding:{}".format(adds))
                    res.append(adds) 
            i-=1
            j+=1
        if s[m] == s[jj]:  
            if s[m] == s[ix] and len(res2) > 0:
                print("ss*={}".format(s[i:j+1]))
                print("m:{}, s[ix]:{}, ix:{}".format(m,s[ix],ix))

                res2.append(s[m:jj+1])
            if len(res2) == 0:
                print("ss={}".format(s[i:j+1]))
                print("m:{}, s[ix]:{}, ix:{}".format(m,s[ix],ix))

                res2.append(s[m:jj+1])
            m-=1 
            jj+=1  
        else:
            break                       
    #print("\n")
    print("res2:{}".format(res2))
    print("res:{}".format(res))  
    if len(res) > 0 and len(res2) == 0:
        return res
    if len(res) == 0 and len(res2) > 0:
        return res2
    if len(res) > 0 and len(res2) > 0:
        return res + res2 
    if len(res) == 0 and len(res2) == 0:
        return []

    
def expandeven(s,ix):
    l = len (s)
    # print("*** ix:{}, h:{}, b:{}, it ={}, s[i] ={} *** ".format(ix,h,b, it, s[ix]))
    i = ix
    j = ix + 1
    res = []
    while i >=0 and j <=l-1:      
        if s[i] == s[j]:
            if s[i] == s[ix] and len(res) > 0:
                # print("ss*={}".format(s[i:j+1]))
                res.append(s[i:j+1])
            if len(res) == 0:
                res.append(s[i:j+1])
                # print("ss={}".format(s[i:j+1]))               
            
        else:
            return res
        i-=1
        j+=1
    return res
                    
                        
# Complete the substrCount function below.
def substrCount(n, s):
    d = {}
    rr = []
    for ix,c in enumerate(s):
        rr.append(c)
        res = expand (s, ix)    
        # res2 = expandeven (s, ix)
        if len(res) > 0:
            print("result:{}".format(res))
            rr = rr + res
    print(rr)
    rcnt = len(rr)
    return rcnt
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
