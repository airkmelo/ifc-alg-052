#ATSM-Alg-052-Ex-10

def prime(k):
    a1 = k%2
    a2 = k%3
    a3 = k%5
    a4 = k%7
    a5 = k%9
    if (a1 == 0 or a2 == 0 or a3 == 0 or a4 == 0 or a5 == 0 or k == 1) and k != 3 and k != 5 and k != 7:
        return "nao primo"
    else:
        for i in range(2, int(k**0.5)+1):
            if k%i==0:
                return "nao primo"
        return "primo"
def main():
    v = int(input("Insira um numero natural: "))
    print(f"O numéro é {prime(v)}")
main()