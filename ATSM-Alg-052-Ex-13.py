#ATSM-Alg-052-Ex-13__live_while_we_young
def monday(m, y):
    if m ==1 or m ==3 or m ==5 or m == 7 or m == 8 or m == 10 or m == 12:
        x=31
    elif m == 4 or m == 6 or m == 9 or m == 11:
        x = 30
    elif m == 2:
        if (y% 400 == 0 or y%100 != 0) and y%4==0:
            x = 29
        else:
            x = 28
    return x
def main():
    mo = int(input("Insira o mes entre 1 e 12: "))
    ye = int(input("Insira o ano: "))
    print(monday(mo,ye))
main()