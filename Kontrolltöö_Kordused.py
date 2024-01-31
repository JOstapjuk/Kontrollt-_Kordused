#Вариант 2
#1
try:
    n=int(input("sisseta arv 1 kuni 9: "))
    if 1<= n <=9:
        for i in range(n):
            print("(\_/)")
            print("(o o)")
            print("/ | \*")
            print(" ")
    else:
        print("arv peab olema vahemikus 1 kuni 9")
except ValueError:
    print("Sisesta korrektne arv")
#2
l=float(input("Sisesta number L: "))
summa=0
number=0
while number<=l:
    summa+=number
    number+=1
print("Numbrirea summa 0 kuni L võrdub",summa)
#3
import random
number=random.randint(0,100)
attempts=10
while attempts>0:
    guess=int(input("Sisesta oma arvamus: "))
    if guess==number:
        print("Te arvasite numbri ära!")
        break
    elif guess<number:
        print("mõistatuslik arv on suurem, proovige uuesti")
    else:
        print("mõistatuslik arv on väiksem, proovige uuesti")
    attempts-=1
if attempts==0:
    print("Vabandage,proove pole enam järel. Mõistatuslik arv oli:",number)
#4
number=int(input("Sisesta täisarv: "))
b=0
while number > 0:
    d=number % 10
    number=number // 10
    b=b * 10 + d
print("Järjestuses vastupidine arv: ",b)
#5
number=int(input("kirjuta täisarv: "))
summa=0
umnoz=1
while number>1:
    d=number%10
    summa+=d
    umnoz*=d
    number= number//10
print("Numbrite summa: ",summa)
print("Arvude esitamine: ",umnoz)
