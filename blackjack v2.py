import random
import time
mast=['Hearts', 'Diamonds', 'Spades', 'Clubs']
naminal = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
ochko={'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
carta= naminal[random.randint(0, len(naminal)-1)] + " of " + mast[random.randint(0, len(mast)-1)]# создали карту

coloda=[] #Создали колоду.
tmp=''
for i in mast:
    for j in naminal:
        tmp+=(j)
        tmp+=(" of ")
        tmp+=(i)
        coloda+=[tmp.split(" ")]
        tmp=''
#Создали колоду.

#Обращение и правила
print("Hello, potato. I'm just a little 'Bender', so let's play Black Jack")
print("im goin 2 take 2 cards. and then ill show u the 2nd one.")
print("After that you must take 2 cards. then u can take one more card. and again...and again... ")
print("Remember: card's denomination give u the same quantity of points. But: pictures give u 10 points, Ace - 11 points")
print("Let's begin")

# Основной класс с картами
class Card:
    def __init__(self, nomercarty):
        self.carta=coloda[nomercarty]
        coloda.remove(self.carta)

#Создаем игрока со стеком
class Player:
    def __init__(self, name, stack):
        self.name = name
        self.stack = stack
    def bet (self, x):
        self.stack-=x
    def win (self, x):
        self.stack+=x
n=input("Write u name: ")
player=Player(n, 1000)


#Дилер берет первый набор карт и говорит информацию

while player.stack>0:
bank=0
ochkodiler=0
kartydilera=[]
for i in range(2):
    diler=Card(random.randint(0, len(coloda)-1))
    ochkodiler+=ochko[diler.carta[0]]
    kartydilera.extend(diler.carta)
    if i ==1:
        print("One of my cards is ", end=" ")
        print(*diler.carta)

time.sleep(5)
print(str(player.name) + ", u stack is " + str(player.stack))
anw = input("Wanna bet? I Multiply bank on 3")
anw = anw.upper()
if anw=="YES" or anw == "Y":
    n=int(input("How much?"))
    player.bet(n)
    bank+=n*3
print("Bank is", bank)
print("Now u take 2 cards. And they're...")
time.sleep(3)

#Игрок берет свой набор карт и видит инфу
ochkogamer=0
kartygamera=[]
for i in range(2):
    gamer = Card(random.randint(0, len(coloda)-1))
    ochkogamer+=ochko[gamer.carta[0]]
    print(*gamer.carta)
    kartygamera.append(gamer.carta)
print("Now u have " +str(ochkogamer) + " points")
print(str(player.name) + ", u stack is " + str(player.stack))



#Запрос на еще карты игроку
while True and ochkogamer<=21:
    ans = input("Wanna take one more?")
    ans=ans.upper()
    if ans=="YES" or ans == "Y":
        anw = input("Wanna bet? I Multiply bank on 2")
        anw = anw.upper()
        if anw == "YES" or anw == "Y":
            n = int(input("How much?"))
            player.bet(n)
            bank += n * 2
        print("Bank is", bank)
        gamer = Card(random.randint(0, len(coloda) - 1))
        ochkogamer += ochko[gamer.carta[0]]
        print("This is", end=" ")
        print(*gamer.carta)
        print("You have " + str(ochkogamer)+ " points.")

    else:
        break

print("I have  " + str(ochkodiler) + " points. This is "+str(' '.join(kartydilera)))

#Условия для добора карт дилером
if ochkodiler<17 and ochkogamer<=21:
    diler = Card(random.randint(0, len(coloda) - 1))
    ochkodiler += ochko[diler.carta[0]]
    kartydilera.append(diler.carta)
    print("I take", end=' ')
    print(*diler.carta)


if (ochkogamer<=21 and ochkogamer>ochkodiler) or ochkodiler>21:
    print("You won")
    print("You have " + str(ochkogamer) +" points. I have "+str(ochkodiler) + " points.")
    print("Bank is", bank)
    player.win(bank)
elif ochkogamer==ochkodiler:
    print("Draw")
    print("You have " + str(ochkogamer) +" points.I have "+str(ochkodiler) + " points.")
elif ochkogamer> 21 or (ochkogamer<ochkodiler and ochkodiler<=21):
    print("I win")
    print("You have " + str(ochkogamer) +" points.I have "+str(ochkodiler) + " points.")
input()





