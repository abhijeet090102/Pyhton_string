ma = 'Hello manisha'
print(ma[:6])
#'Hello '
print(ma[5:])
#' manisha'
print(ma[:5]+ma[5:])
#'Hello manisha'
print(ma[:16])
#'Hello manisha'
print(ma[16:])
#''
print(ma[16:]+ma[:16])
#'Hello manisha'
print(ma[5:8])
#' ma'
print(ma[6:9])
#'man'
print(ma[6:None])
#'manisha'
print(ma[0:len(ma):2])
#'Hlomnsa'
print('m' in ma)
#True
print('s' in ma)
#True
space = ''
for i in ma:
    space += i + ' '
print(space)
