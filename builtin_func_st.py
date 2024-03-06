st = 'Hello Manisha'
print('"a" appears',st.count('a'))
vowel = 'aeiou'
counst = 0
for i in vowel:
    counst += vowel.count(i)
print('vowels are',counst)

am = 'red , green , blue , red, yellow , red , white , blue'
#find and rfind : find return first appear index of a string in another string and rfind returns the last occurence of a string in another string
print('index first appear no ',am.find('red'))
# returns index no 0
print(am.find('green')) #returns the index no 6
print('last appear index no ',am.rfind('blue'))

''' capitalize , title , lower , upper and swapcase'''
# capitalize transforming into a sentence case in string
ma = input("Enter any string :")
print('CAPITALIZED FORM ',ma.capitalize())
# title convert the first letter of each word into captialze .
print('title form ',ma.title())
# lower and upper used to convert all leter's in a string to lowercase and uppercase
print('lower form ',ma.lower())
print('UPPER FORM ',ma.upper())
''' swapcase used to convert lowercase letter in a string to uppercase and vise versa'''
print('SWAPPING CASE ',ma.swapcase())

''' islower ,isupper, and istitle "
islower and isupper can used to check if all letters in a string are in lowercase
or uppercase , respectively '''
print('CHEACKING LOWER CASE ','python'.islower())
print('CHEACKING UPPERCASE','PYTHON'.isupper())
print('CHECKING TITLE',st.istitle())
print('Abhijeet 09'.istitle())

''' replace : replace allows to replace part of a string by another string , it takes two arguments '''
message = 'Am is our love , Am is a our title'
print('REPLACING ANY STRING ',message.replace('our','lovely'))

''' strip , lstrip , rstrip '''
print('REMOVING SPACE ','     Hello how are you     '.strip())

''' split and partition
split : used for split a string into a list of string based on a delimiter
partition :  divides a string s into two parts based on a delimiter
and returns a tuple'''

amst = 'Hello, How, are, you?'
print(amst.split())
print('hello . how are you?'.partition('.'))

''' join return a string comprising elements of a sequence separated
by the specified delimiter '''
print('>'.join(['I' , 'am' , 'ok']))
print(' '.join(['I' , 'love','you' , 'my','love']))

''' isspace , isalpha , isdigit , and isalnum eanbles to check whether a value
is of desire type.'''
print(ma.isalpha())
mabno = input('Enterr mobile no')
print(mabno.isdigit() and len(mabno) == 10)
print(ma.isspace())

'''isalnum checks whether a string compries of alphabet and digits only
. if the password is allowed to comprise of only alphabets and digits. '''
password = input("Enter password ")
print('CHEACKING PASSWORD ',password.isalnum())

''' startswith and endswith'''
name = 'Abhijeet karmakar'
print('check last name ',name.endswith('karmakar'))
print('check first name',name.startswith('Abhijeet'))

''' encode and decode
sometimes we need to transform data from one format to another for the sake of
compatibility'''
# encode : that returns the encoded version of tring
mats = 'Hello i am abhijeet'
ts = mats.encode('utf32')
print('encoded form in utf32',ts)
en_ts = mats.encode('utf16')
print('encoded in utf16',en_ts)
#decode : reverse of function encode
print('Decoded version utf32',ts.decode('utf32'))
