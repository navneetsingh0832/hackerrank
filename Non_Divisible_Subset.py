import math
import os
import random
import re
import sys

def nonDivisibleSubset(k, s):
    # Write your code here
    f=[0]*k
    for ele in s:
        r=ele%k
        f[r]+=1
    if(k%2==0):
        f[k//2]=min(f[k//2],1)
    ans=min(f[0], 1)
    for i in range(1, (k//2)+1):
        ans+=max(f[i], f[k-i])
    return ans
