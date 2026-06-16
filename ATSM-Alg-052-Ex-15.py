#ATSM-Alg-052-Ex-15

def hex2int(x):
    t = 0
    c = 0
    x = x[::-1]
    for i in x:
        y = ord(i)
        if 48 <= y <= 57:
            x = int(i)
            t = t + x*(16**c)
        elif 65 <= y <= 70 or 97 <= y <= 102:
            if y == 65 or y == 97:
                t = t + 10*(16**c)
            elif y == 66 or y == 98:
                t = t + 11*(16**c)
            elif y == 67 or y == 99:
                t = t + 12*(16**c)
            elif y == 68 or y == 100:
                t = t + 13*(16**c)
            elif y == 69 or y == 101:
                t = t + 14*(16**c)
            elif y == 70 or y == 102:
                t = t + 15*(16**c)
        c=c+1
    return t

def int2hex(x):
    t = ""
    x = int(x)
    while x > 0:
        
        l = x % 16
        x = x // 16
        l = int(l)
        x = int(x)
        if 0 <= l <= 9:
            y = str(l)
            t = y + t
            l = int(y)
        elif 10 <= l <= 15:
            if l == 10:
                t = "A"+t
            elif l == 11:
                t = "B"+t
            elif l == 12:
                t = "C"+t
            elif l == 13:
                t = "D"+t
            elif l == 14:
                t = "E"+t
            elif l == 15:
                t = "F"+t
    return  t

def main():
    n = input("Insira seu número(dec ou hex):")
    c = input("Converter para((dec) ou (hex)):")

    if c == "dec":
        print(hex2int(n))
    elif c == "hex":
        print(int2hex(n))
main()