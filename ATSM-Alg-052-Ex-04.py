#ATSM-Alg-052-Ex-04

def mediana(x,y,z):
    a = min(x,y,z)
    c = max(x,y,z)
    b = (x+y+z)-(a+c)
    return b
def main():
    i1 =int(input())
    i2 =int(input())
    i3 =int(input())
    print("Mediana é", mediana(i1,i2,i3))
main()