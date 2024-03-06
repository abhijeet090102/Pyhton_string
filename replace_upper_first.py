def upper_first(am):
    
    st = ''
    for i in range(len(am)):
        if i ==0 or am[i-1] == ' ' :
            st += chr(ord(am[i])-32)
        else:
            st += am[i]
    return st

am = input('Enter any sentence ')
print(upper_first(am))
