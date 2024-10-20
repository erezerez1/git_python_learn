# ex 9-13 dice
import random


class cube ():
    def __init__(self,num_dies):
        cube.num_dies = num_dies
    def roll(self):
        result=random.randint(1,6)
        print(f"rolled and got {result}")
              
mycube=cube(6)
for i in range(1,6):
    mycube.roll()
print("just finished")


# ex 9-14
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits="1234567890"
myseq=[]
for i in range(1,10):
    nextitem=random.choice(uppercase_letters)
    print(f"next item: {nextitem}")
    myseq += nextitem

for i in range(1,5):
    nextitem=random.choice(digits)
    print(f"next item: {nextitem}")
    myseq += nextitem

print(f"the results is {myseq}")
print("".join(myseq))


