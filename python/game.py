from random import randint
def rand3():
    return randint(100, 1000)
rd= rand3()
print("WELCOME TO THE NUMBER GUESSING GAME")
print("Only 3digit number would be there")
c=rd%10
b=int((rd%100-c)/10)
a=int((rd-rd%100)/100)
g=0
while g==0:
    num=int(input("Enter your number to guess"))
    f=num%10
    e=int((num%100-f)/10)
    d=int((num-num%100)/100)
    if num==rd:
        print("CODE CRACKED")
        g=1
    elif d==a or e==b or f==c:
        print("MATCH")
    elif d==b or d==c or e==a or e==c or f==a or f==b:
        print("CLOSE")
    else:
        print("NOPE")
