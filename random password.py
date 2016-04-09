


import string
import random
print ('Random Password')
print ('---------------')
print
def randompassword():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    size= 0

    return ''.join(random.choice(chars) for x in range(size,30))

print(randompassword())
print
print ('30 characters')
print
def randompassword2():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits
    size= 0

    return ''.join(random.choice(chars) for x in range(size,60))

print(randompassword2())
print
print ('60 characters')
