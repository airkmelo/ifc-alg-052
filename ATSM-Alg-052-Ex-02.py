#ATSM-Alg-052-Ex-02

def taxi_tarif(km):
    d = km*1000
    p = 4 + (0.25*d)/140
    return p
def main():
    d = float(input())
    print(taxi_tarif(d))
main()