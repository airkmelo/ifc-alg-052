#ATSM-Alg-052-Ex-14__bye_bye_bye

def magicda(d,m,y):
    y = str(y)
    t = ""
    for i in range(1,3):
        z = y[-i]
        t = z + t
    y = int(t)
    x = d * m
    if x == y:
        return True
    else:
        return False
    
def main():
    print("Século XIX")
    d = int(input("Insira o dia(dd): "))
    m = int(input("Insira o mes(mm): "))
    y = int(input("Insira o ano(yyyy): "))
    print("Data Mágica: ", (magicda(d,m,y)))

    for yy in range(1900, 2000):
        for mm in range(1, 13):
            if mm == 2:
                if yy % 4 and (yy%100 != 0 or yy&400==0):
                    dd = 29
                else:
                    dd = 28
            elif mm == 4 or mm == 6 or mm == 9 or mm == 11:
                dd = 30
            else:
                dd = 31
            for dy in range(1, dd+1):
                k = magicda(dy,mm,yy)
                if k == True:
                    print(f"{dy:02d}/{mm:02d}/{yy}")
            
main()