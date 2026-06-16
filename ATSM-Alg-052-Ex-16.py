#ATSM-Alg-052-Ex-16

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

def binary2int(x):
    no = x
    no = no[::-1]
    x = 0
    v = 0
    for i in no:
        no = int(i)
        v = v + (2**x)*no
        x = x + 1
    return v

def int2binary(x):
    x = int(x)
    qoqo = x
    r = 0 
    result = ""
    while qoqo != 0 :

        r = qoqo % 2
        qoqo = qoqo // 2
        r = str(r)
        result = r + result
    return result


def int2arb(num, bas):

    chc = "0123456789ABCDEF"
    num = int(num)
    if num == 0:
        return "0"
    rsl = ""

    while num > 0:

        r = num % bas
        rsl = chc[r] + rsl
        num = num // bas
    return rsl

def arb2int(num, bas):

    chc = "0123456789ABCDEF"
    num = num.upper()
    pot = 0
    t = 0
    num = num[::-1]

    for i in num:

        v = chc.index(i)
        t = t + v * (bas ** pot)
        pot = pot + 1
    return t

def main():
    n = input("Insira seu número(dec ou hex ou bin ou arbitrario):")
    c = input("Converter ((hex2int) ou (int2hex) ou (int2bin) ou (bin2int) ou (int2arb) ou (arb2int):")

    if c == "hex2int":
        print(hex2int(n))
    elif c == "int2hex":
        print(int2hex(n))
    elif c == "int2bin":
        print(int2binary(n))
    elif c == "bin2int":
        print(binary2int(n))
    elif c == "int2arb" or c == "arb2int":
        b = int(input("Insira a base: "))
        if c == "int2arb":
            print(int2arb(n,b))
        else:
            print(arb2int(n,b))
main()