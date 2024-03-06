am = 'abhijeet'
st = ''
for i in am:
    if i in st:
        st += '*'
    else:
        st += i
print(st)
