

#How to potenitally score boggle

def p(word):
    if len(word) < 8: return {'3':1,'4':1,'5':2,'6':3,'7':5}[str(len(word))]
    elif len(word) >= 8: return 11
    else: return 0

#Out of class declare function to start boggle Board and set points to 0
