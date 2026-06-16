#ATSM-Alg-052-Ex-09

def isIntenger(ex):
    t = ""
    for i in ex:
        if i == " ":
            None
        else: 
            t = t + i
    
    if len(t) >= 1:
        if t[0] == "+" or t[0] == "-" or t[0] == "1" or t[0] == "2" or t[0] == "3" or t[0] == "4" or t[0] == "5" or t[0] == "6" or t[0] == "7" or t[0] == "8" or t[0] == "9" or t[0] == "0" :
            x = 0
            y = 0
            for i in t:
                if y == 0:
                    None
                else:
                    if i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9" or i == "0":
                        x +=1  
                y +=1
            if x == (len(t)-1):
                return True
            else:
                return False
        else:
            return False      
    else:
        return False
    
def main():
    t = input()
    print("O resultado é: ", isIntenger(t))
main()