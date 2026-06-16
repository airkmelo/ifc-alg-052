#ATSM-Alg-052-Ex-07

def trian(x,y,z):
    a = max(x,y,z)
    b = min(x,y,z)
    c = (x + y + z)-(a + b)
    if a >= (b+c):
        return False
    else:
        return True
    
def main():
    x = int(input("Insira o valor 1: "))
    y = int(input("Insira o valor 2: "))
    z = int(input("Insira o valor 3: "))
    t = trian(x,y,z)
    if t == True:
        print("Triangulo valido")
    else:
        print("Triangulo invalido")

main()