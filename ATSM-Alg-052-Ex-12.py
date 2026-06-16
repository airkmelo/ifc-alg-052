#ATSM-Alg-052-Ex-12

import random as r

def ranpassval():
    x=0
    w=0
    y=0
    z=0
    k = r.randint(7,10)
    t = ""
    for i in range(k):
        p = r.randint(33,126)
        t = t + chr(p)
    if len(t)>=8:
            w +=1
    for i in t:
        if 65 <= ord(i) <= 90:
            x+= 1
        elif 97 <= ord(i) <= 122:
            y+= 1
        elif 48 <= ord(i) <= 57:
            z+=1
    if x>= 1 and y >= 1 and z >= 1 and w >= 1:
        return True, t
    else:
        return False, t
    
def main():
    print(ranpassval())
main()