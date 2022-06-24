import random
def game():
    print(" welcome ")
    print("star game")
    name=input("enter your name  >>>>")
    num=set()
    i=1
    while i<=5:
        num.add(random.randint(0,9))
        if len(num)!=5:
            num.add(random.randint(0,9))
        if len(num)==5:
            break
        i=i+1
    list1=list(num)
    print(list1)
    chance=5
    i=0
    cow=0
    bull=0
    a=[]
    b=[]
    while 1<=chance:
        guess=int(input("enter the guess number >>>>"))
        position=int(input("enter the position >>>>>"))
        b.append(position)
        print("you have only",chance,">>>>")
        if guess in list1:
            a.append(guess)  
            if b[i]==list1.index(guess):
                bull+=1
                print(bull,"bull")
            else:
                cow+=1
                print(cow,"cow")
        if len(a)==len(list1)==len(b)==5:
            break
        chance-=1
        i+=1
    if cow<=1:
        print(f"Congratulations {name} You are the winner")
    else:
        print("Opps You are the looser ")
   
    play=input("play again enter ( yes/no ):")
    if play=="yes":
        game()
    else:
        return "exit"
print(game())
