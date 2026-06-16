#ATSM-Alg-052-Ex-05

def ordinal(n):
    if 1<=n<=12:
        if n == 1:
            return "primeiro"
        elif n == 2:
            return "segundo"
        elif n == 3:
            return "terceiro"
        elif n == 4:
            return "quarto"
        elif n == 5:
            return "quinto"
        elif n == 6:
            return "sexto"
        elif n == 7:
            return "sétimo"
        elif n == 8:
            return "oitavo"
        elif n == 9:
            return "nono"
        elif n == 10:
            return "décimo"
        elif n == 11: 
            return "décimo primeiro"
        elif n == 12: 
            return "décimo segundo"
    else:
        return ""
    
def main():
    i = int(input())
    print(ordinal(i))

main()