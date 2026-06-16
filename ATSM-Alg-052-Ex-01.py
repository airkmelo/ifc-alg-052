#ATSM-Alg-052-Ex-01

def hipotenusa(a, b):
    c = (a**2 + b**2)**0.5
    return c
def main():
    a1 = float(input())
    a2 = float(input())
    print(hipotenusa(a1,a2))
main()