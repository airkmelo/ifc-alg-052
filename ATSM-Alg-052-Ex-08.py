#ATSM-Alg-052-Ex-08

def upper(ph):
    t2 = ""
    c = 0
    x = 0
    for i in ph:
        t = ord(i)
        if x == 0:
            if 97 <= t <= 122:
                t2 = t2 + i.upper()
            else:
                t2 = t2 + i
        else: 
            if t == 46 or t == 33 or t == 63:
                c = 1
                t2 = t2 + i
            else:
                if c == 1 and i != " ":
                    t2 = t2 + i.upper()
                    c = 2
                else:
                    t2 = t2 + i
        x+=1
    return t2
        
def main():
    st = input("Insira sua frase:")
    print(upper(st))
    
main()