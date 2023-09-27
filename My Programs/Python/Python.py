def fun(input):
    print("Good Mornig Sir: "  +input)
a=fun(input("Enter your name1 "))
b=fun(input("Enter your name2 "))
c=fun(input("Enter your name3 "))
##########################################################
PROJECT: 1
import random

def GAME(computer,me):
    if computer==me:
        return None
    if computer=='s' or me=='w':
        return False
    elif computer=='s' or me=='g':
         return True
    if computer=='w'or me=='g':
        return False
    elif computer=='w' or me=='s':
        return True
    if computer=='g' or me=='s':
        return False
    elif computer=='g' or me=='w':
        return True 

print("computer turn: Snake(s),Water(w),Gun(g)")
random=random.randint(1,3)
if random==1:
    computer='s'
elif random==2:
    computer='w'
elif random==3:
    computer='g'

me=input("my turn: Snake's', Water'w', Gun'g'" )
a=GAME(computer,me)
print(f"Computer Chose : {computer}")
print(f"You Chose : {me}")
if a==None:
    print("The Game Is Tie")
elif a==True:
    print("You Lose")
elif a==False:
    print("You Win")
##########################################################
#PROJECT 1.2
def GAME(p1,p2):
    if p1==p2:
        return None
    if p1=='s' or p2=='w':
        return True
    elif p1=='s' or p2=='g':
        return False
    if p1=='w' or p2=='g':
        return True
    elif p1=='w' or p2=='s':
        return False
    if p1=='g' or p2=='s':
        return True
    elif p1=='g' or p2=='w':
        return False

p1=input("P1 Turn: Snake(s),Water(w),Gun(g)")
p2=input("p2 Turn: snake(s),water(w),Gun(g)")

a= GAME(p1,p2)

if a==None:
    print("The Game Is Tie.")
elif a==True:
    print("Player 1 is Winner.")
elif a==False:
    print("Player 2 is Winner.")
#########################################################
#Dictionary
print("***Welcome to Oxford Dictionary***")
dec={"Apple" :"Fruit",
     "Carrot":"Vegetable",
     "Cat"   :"Animal",
     "Parrot":"Bird",
     "Tesla" :"Car"
}
user=input("Enter the word:  ")
if user in dec.keys():
    print(f"The meaning of your word is:  {dec.get(user)}") 
elif user != dec:
    print("The meaning of your word is not avaliable")
    with open ('new.txt','w') as f:
        word=f.write(user)
#########################################################
