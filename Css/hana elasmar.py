print("My name ia hana")
print("I am 22 years old")
print("I studed computer science ")
print("I studied it for 4 years")
print("I gratuaded from damietta university")
print("I worked in salam company")
print("I had a trainship in anthor company")
print("My hoppies is :swimming and reading in programming")
print("I am currently taking a course in IT")
print("I will be happy to be a part from your company")
#VARIABLES.PY
name="hana elasmar"
age=22
money=4000.9
happy="yes"
print(name)
print(age)
print(money)
print(happy)
print("name: "+name)
print("Age: "+str(age))
print("money: "+str(money))
first="hana"
last="elasmar"
full_name=first+""+last
print(f"2**3={2**3}")
x=6
z=x+2
print(z)
x=8
y=4
c=x-2*y
print(c)
p=1
n=p+2
m=p**n
print(m)
v=10
i=2
k=v/i
print(k)
j=13
o=3
p=j%o
print(p)
c=5
c=c+5
c+=5
c-=3
c*=2
c/=5
c%=1
print(c)
print(5==2)
print(5!=2)
print(5>3)
print(5<3)
print(5>=3)
print(5>4 and 5>7)
print(5<9 and 9<15)
print(2>1 or 4<2)
print(3>7 or 5>8)
print(5>3 and 5>2,",",5>2)
# data_type.py
t=[1,2,3]
print(type(t))
print(t[2])
print(t.index(2))
t.append(4)
print(t)
t.remove(1)
print(t)
t[2]=0
print(t)
s=(3,7,1)
print(type(s))
print(s.index(7))
e=("green","red","blue")
print(e.count("red"))
print(e.count("pink"))
v=(23,"abc",4.56,(2,3),"def")
print(v[0:-1])
#input.py
#h=input("name:")
#a=input("age:")
n=input("how much money do you want?")
#a=input("Are you happy?")
#k=input("What are your hoppies?")
#h=input("Talk about your self more")
#a=input("Are you work with team")
#l=input("What are your stenghts?")
#e=input("What are your weakness?")
#d=input("Why should i hire you?")
#e=input("What do you do in your free time?")
#l=input("Can you give an advice for high school graduates? ")
#a=input("Why you chosse computer science?")
#s=input("Where do uou see your self the next 5 years from now?")
#m=input("Can you handle with deep stress?")
#a=input("What is your ambitions in our company?")
#r=print("Thank you ")
#g=float(input("entre x="))
#f=float(input("entre y=")
#z=g+f
print("###")
#if.py
x=float(input("x="))
if 0<=x<10:
    print("x**3")
elif 10<=x<20:
    print("x**2")
else:
    print("2x")
num=10
if num%2==0:
    print("even num")
else:
    print("odd num")
value=int(input("entre a value:"))
if value>=0 and value<=100:
    print("you typed ",value)
h=float(input("entre the age")) 
if h>=18:
    print("you can vote")  
else:
    print("you canot vote")
money=float(input("my money="))
if money<1000:
    print("you need money")
elif money==1000:
    print("do you need money?")
else:
    print("you are rich")
he_is_hungry=True
has_money=True
restaurant_open=True
if he_is_hungry and has_money and restaurant_open:
    print("I want food")
else:
    print("i am in my diet")
iam_in_agoodmood=True
clupisopen=False
free=False
if iam_in_agoodmood and clupisopen and free:
    print("I am hungry")
else:
    print("i will stay in home")
Icook_our_food=True
go_to_dry_clean=True
have_alot_of_work=False
if Icook_our_food and go_to_dry_clean or have_alot_of_work:
    print("i will go to my mum")
else:
    print("go to bed")
day=input("entre the day")
if day=="saturday"or day=="friday":
    print("it is holiday")
else:
    ("go to work")
a=float(input("entre a="))
b=float(input("entre b="))
if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal b")
else:
    print("b is greater than a")
a=float(input("x="))
if x>0:
    print("x is positive")
elif x<0:
    print("x is negative")
else:
    print("x=zero")
h=float(input("entre the height in (meters):"))
w=float(input("entre the weight in (kg):"))
bmi=w/(h**2)
if bmi<=18.5:
    print("under weight")
elif 18.5<bwi<=24.5:
    print("normal weight")
elif 25<=bmi<=29.5:
    print("over weight")
else:
    print("obesiyt")
year=int(input("the year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("it is a leap tear")
        else:
            print("it is a simple year")
    else:
        print("it is a leap")
else:
    print("it is a holiday")
t=[2,5,9,8,1]
max_num=5
min_num=2
for num in t:
    if num>max_num:
        max_num=num
    if num<min_num:
        min_num=num
print(f"the max num is:{max_num}")
print(f"min num is:{min_num}")
print(float(max_num+min_num))
correct_password="hana"
while True:
      password=input("entre the password=")
      if password==correct_password:
            print("true")
            break
      else:
            print("false")  
n=2
primes=[]
for i in range(2,n+1):
      for z in range(2,int(i**0.5)+1):
        if i%z==0:
              break
else:
     primes.append(i)
print(primes) 
num=int(input("entre the number="))   
      



























        










