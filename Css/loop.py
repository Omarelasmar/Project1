for number in range(1,6):
    print(number)
print("###")
for letters in "yahya":
        print(letters)
print("###")
for x in range(1,5):
      for y in range(1,6):
            print(x,y)
print("###")
h=[1]
s=10
for j in h:
      s*=j
      print(s)
print("###")
t=[7,1,4,3]
for u in t :
      print(u+3)
print("###")
k=[1,3,2,4,5]
s=0
for y in k:
      s+=y
      print(s)
print("###")
for c in range (2):
      print("hello python")
print("###")
for l in range(2,21,2):
      print(l)
print("###")
for n in range(1,22,2):
      print(n)
print("###")
for i in range(1,6):
      for j in range(1,6):
            print(f"{i}*{j}={i*j}")
print("###")
sum=0
for numbers in range(8):
      sum=sum+numbers
print(sum)
print("###")
myhoppies= ("reading""30%","swimming""50%","skating""20%" )
for hoppies in myhoppies:
      print(f"my hoppies are{myhoppies}:{myhoppies}")
      break
print("###")
#o=int(input("entre the number"))
#for b in range(o):
     # print(b+6)
print("###")
#correct_password="hana60"
#entered_password=input("entre the password:")
#while entered_password !=correct_password:
      #print("incorrect_password.try again:")
#print("access granted")
print("###")
name="mona"
for p in name:
      print(F"this letters {p.upper()}")
print("###")
colors=["red","blue","green"]
for y in colors:
      print(y)
print("###")
colors=["red","blue","green"]
for w in colors:
    if w=="blue":
         print(f"my favourite colors is {w}")
    else:
        print(w)
print("###")
i=1
while i <6:
      print(i)
      i+=1
print("###")
i=1
while i<6:
      i+=1
      print(i)
print("###")
i=1
while i<6:
      i+=1
      if i ==3:
            continue
      print(i)
print("###")
i=1
while i<6:
      i+=1
      if i==5:
            break
      print(i)
print("###")
i=1
while i<6:
      print(i)
      i+=1
else:
      print("the condition is not true")
print("###")
#value=input("type less than 6 letters:")
#num=1
#for letter in value :
      #print("letter",num,"is",letter)
      #num+=1
#else:
      #print("empty")
print("###")
for i in range(5,0,-1):
      print(i)
print("###")
for v in range(5,10,2):
      print(v)
print("###")
n=2
primes=[]
for i in range(2,n+1):
      for z in range(2,int(i**0.5)+1):
        if i%z==0:
              break
else:
     primes.append(i)
print(primes)
print("###")
s=[]
k=0
while(2**k<=1024):
      s.append(2**k)
      k=k+1
print(s)
print("###")
k,sum=0,0
while(2**k<=60):
      sum+=(2**k)
      k=k+1
print(sum)
print("###")
sum=0
for k in range(1,15,2):
      sum+=(k**3)
print(sum)
print("###")
#n=int(input("entre the num:"))
#actorial=1
#while n>0:
    #factorial*=n
    #n=-1
#print("factorial:",factorial)
print("###")
num=123
count=0
for digit in str(num):
      count+=1
print("the num of digits is :",count)
print("###")
mylist=[1,2,3,4]
nl=[]
for num in mylist:
      nl.append(num**2)
print(nl)
print("###")
#max_miles=int(input("entre  the max of miles"))
#print("miles\t\tkm")
#for miles in range(1,max_miles+1):
      #km=miles*1.6
      #print(f"{miles}mile(s)\t{km}km")
print("###")
#while True:
     # x=int(input("entre the value of t="))
     # break
print("###")
n=1
while n<3:
      print(n)
      n=n+1
print("###")
n=1
while n<5:
      n=n+1
      print(n)
print("###")
limit=int(input("entre the limit:"))
total=0
i=1
while i<=limit:
      total+=1
      i+=1
print(total)
print("###")
n=int(input("entre a num:"))
factorial=1
while n>0:
      factorial*=n
      n-=1
print("factorial:",factorial)
print("###")
correct_password="hana"
while True:
      password=input("entre the password=")
      if password==correct_password:
            print("true")
            break
      else:
            print("false")
print("###")
max_milles=int(input("entre the maximum number of milles:"))
print("miles\t\tkm")
for miles in range(1,max_milles+1):
      km=miles*1.609
      print(f"{miles}mile(S)\t{km} km")   
print("###")
h=[1,2,3,4]
nl=[]
for i in range(4):
      nl.append(h[i]**2)
print(nl)


``









      