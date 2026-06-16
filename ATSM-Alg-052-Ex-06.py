#ATSM-Alg-052-Ex-06


def impr(st, nmr):
    a = len(st)
    c = (nmr-a)//2
    for i in range(c):
        st = " " + st
    return st
def main():
    s = input()
    n = int(input())
    print("*"*n)
    print(impr(s, n))
    print("*"*n)
main()