"""
myfavorites=['maldives', 'sychelles', 'koh samui']
print(myfavorites)
myfavorites.sort()
print(myfavorites)
myfavorites.reverse()
print(myfavorites)
newl=sort(myfavorites)
print(newl)


squares = []
for i in range(10):
    squares.append(i*i)
print(squares)

squares = []
i=10
while i>0 :
    squares.append(i * i)
    i=i-1
print(squares)


uinput=input()
if (int(uinput)==1):
    print("its one")
elif (int(uinput)==2):
    print("its two")
else:
    print("some other number")


class fridge:
    def __init__(self,maker,volume):
        self.maker=maker
        self.volume=volume

    def set_volume(self,newv):
        self.volume=newv

    def print_fridge(self):
        print(f"fridge maker is {self.maker}")
        print(f"fridge volume is {self.volume}")

newf=fridge("amcor",600)
newf.print_fridge()

"""
x = "welcome"
#if condition returns False, AssertionError is raised:
assert x != "hello", "x should be 'hello'"
print("the run continues")