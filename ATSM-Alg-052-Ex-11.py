#ATSM-Alg-052-Ex-11

import random as r

def ranpass():
    k = r.randint(7,10)
    t = ""
    for i in range(k):
        p = r.randint(33,126)
        t = t + chr(p)
    return t

def main():
    print(ranpass())
main()