#import Tkinter
#top = Tkinter.Tk()
#top.mainloop()

import string
import random
print ('5 Random Password')
print ('-----------------')
print
x = input('lengte:')
def randompassword():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + '!@#$%^&*()'
    size= 0

    return ''.join(random.choice(chars) for x in range(size, +x))

print(randompassword())
print(randompassword())
print(randompassword())
print(randompassword())
print(randompassword())

print

raw_input("Press Enter to Exit")

