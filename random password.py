import Tkinter
import string
import random
#top = Tkinter.Tk()
#top.geometry('300x200-5+30')
#oldtitle = top.title()
#top.title('5 Random Passwords')
#top.mainloop()




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

print

raw_input("Press Enter to Exit")





