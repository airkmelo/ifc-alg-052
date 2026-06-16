#ATSM-Alg-052-Ex-03

def ecommerce(a):
    x = 4 + (0.25/140)*(a*1000)
    return x

def main():
    i = int(input("Insira sua distancia: "))
    print(ecommerce(i))

main()