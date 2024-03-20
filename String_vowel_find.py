
'''st = input("enter input string: ")
sp = 0
word = 0
vo  = 0
v = "aeiouAEIOU"
for i in (st):
    word+= 1
    if i==" ":
        sp=sp+1
    if i in v:
        vo+=1
print (vo)
print("space=",sp)
print("word=",word)'''
v = "aeiouAEIOU"
co = 0
st = input("enter input : ")
for i in st:
    if i>='A' and i <='Z' or i >='a' and i<='z':
        if i not in v:
            co +=1
print(co)