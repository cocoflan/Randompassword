


import string
import random
print ('Random Password')
print ('---------------')
print
x = input('lengte:')
def randompassword():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    size= 0

    return ''.join(random.choice(chars) for x in range(size, +x))

print(randompassword())
print
print
y = input('lengte:')
def randompassword2():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    size= 0

    return ''.join(random.choice(chars) for x in range(size, +y))

print(randompassword2())
print
