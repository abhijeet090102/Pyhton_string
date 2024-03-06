 # occurence strings
i = 0
a = 0
m = 0
for i in range(len(message)-1):
    if message[i] == 'a' :
        a +=1
    if message[i+1] =='m':
        m += 1
print("no of a occured ",a)
print(" no of times m occured",m)

message = 'abhijeet is a impressive man'
message.count('a','m')
