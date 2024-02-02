##Вариант 2
##1
#try:
#    n=int(input("sisseta arv 1 kuni 9: "))
#    if 1<= n <=9:
#        for i in range(n):
#            print("(\_/)")
#            print("(o o)")
#            print("/ | \*")
#            print(" ")
#    else:
#        print("arv peab olema vahemikus 1 kuni 9")
#except ValueError:
#    print("Sisesta korrektne arv")
##2
#l=float(input("Sisesta number L: "))
#summa=0
#number=0
#while number<=l:
#    summa+=number
#    number+=1
#print("Numbrirea summa 0 kuni L võrdub",summa)
##3
#import random
#number=random.randint(0,100)
#attempts=10
#while attempts>0:
#    guess=int(input("Sisesta oma arvamus: "))
#    if guess==number:
#        print("Te arvasite numbri ära!")
#        break
#    elif guess<number:
#        print("mõistatuslik arv on suurem, proovige uuesti")
#    else:
#        print("mõistatuslik arv on väiksem, proovige uuesti")
#    attempts-=1
#if attempts==0:
#    print("Vabandage,proove pole enam järel. Mõistatuslik arv oli:",number)
##4
#number=int(input("Sisesta täisarv: "))
#b=0
#while number > 0:
#    d=number % 10
#    number=number // 10
#    b=b * 10 + d
#print("Järjestuses vastupidine arv: ",b)
##5
#number=int(input("kirjuta täisarv: "))
#summa=0
#umnoz=1
#while number>1:
#    d=number%10
#    summa+=d
#    umnoz*=d
#    number= number//10
#print("Numbrite summa: ",summa)
#print("Arvude esitamine: ",umnoz)

#v1 1
#while True:
#    try:
#        mitu=int(input("Mitu tk: "))
#        if 1<=mitu<10:
#            break
#    except ValueError:
#        print("Vale tüüp")
#for i in range(mitu):
#    print('  /V\  '.center(10,' '),end="")
#for i in range(mitu):
#    print(' / V \ '.center(10,' '),end="")
#for i in range(mitu):
#    print(' / V V \ '.center(10,' '),end="")
#for i in range(mitu):
#    print(' /VV V VV\ '.center(10,' '),end="")

##v4 5
from random import *
#sum_num=0
#sum_km=0
#for i in range(12):
#    num=randint(1000,10000)
#    km=randint(1,1000)
#    sum_num+=num
#    sum_km+=km
#    print(f"{i}. maakond. \nElanikud: {num}. Pindala: {km}\n. Kokku: {sum_num},{sum_km}")
#vastus=sum_num/sum_km
#print(vastus)

#v5 2
#n=25
#kesk1=0
#kesk2=0
#for i in range(n):
#    h1=randint(1,5)
#    h2=randint(1,5)
#    kesk1+=h1
#    kesk2+=h2
#kesk1/=n
#kesk2/=n
#print("keskmine hine 1 klassis on ",kesk1," keskmine hinne 2 klassis on ",kesk2)

#v4 5
pann=0
lisapann=0
while True:
    try:
        k=int(input("Mitu kotleti sul on: "))
        if k>0:
            break
    except ValueError:
        print("Vale tüüp")
while True:
    try:
        m=int(input("Mitu kotleti ühel pannil? "))
        if m>0:
            break
    except ValueError:
        print("Vale tüüp")
while k>0 and k>=m:
        k-=m
        pann+=1
        if k<m:
            lisapann+=1
print("täispannid: ",pann," ja veel on vaja",lisapann," pannid")
