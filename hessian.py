import time
import numpy as np
import matplotlib.pyplot as plt
import random

def equ(D,p,x,y):
  #X*X*X+Y*Y*Y+1=D*X*Y
  for i in range(0,p):
    for j in range(0,p):
      if(((D*i*j)%p)==((i*i*i+j*j*j+1)% p)):
      	y.append(j)
      	x.append(i)
  print(x)
  print(y)
  return 

def encode(inp,k,x,p): 
  Dict={}
   	
  for i in range(33,65):
    c=chr(i)
    Dict.update({c:k})
    k=k+1 
  
  for i in range(97,123):
    c=chr(i)
    Dict.update({c:k})
    k=k+1
  for i in range(65,91):
    c=chr(i)
    Dict.update({c:k})
    k=k+1
  print(Dict[inp])

def point_add(X1,X2,Y1,Y2):
  A = X1*Y2
  B = Y1*X2
  X3 = B*Y1-Y2*A
  Y3 = X1*A-B*X2
  Z3 = Y2*X2-X1*Y1
  return tuple((X3,Y3))

def doubling(X1,X2,Y1):
  A=X1*X1
  B=Y1*Y1
  D=A+B
  z=X1+Y1
  G=z*z-D
  X3 =((2*Y1)-G)*(X1+A+1)
  Y3 =(G-(2*X1))*(Y1+B+1)
  Z3 =(X1-Y1)*(G+(2*D))
  return tuple((X3,Y3))


#Encryption
def encrypt(x,y,k,n2,ra):
  l=0
  m=0
  print("*****Encrypting******")
  for i in range(1,k+1):
    x1=x[ra]
    y1=y[ra]
      
    if(i==2):
      x2=x1
      l,m=doubling(x1,x2,y1)
    elif (i>2):
      (l,m)=point_add(l,x1,m,y1)
  print("K*G:",l,m)

  for i in range(1,n2+1):			#nb=n2
    x1=x[ra]
    y1=y[ra]
    if(i==2):
      x2=x1
      p,q=doubling(x1,x2,y1)
    elif (i>2):
      (p,q)=point_add(p,x1,q,y1)
  print("Pb:",p,q)			#Public key of user b

  for i in range(1,k+1):			
    x1=p
    y1=q
    if(i==2):
      x2=x1
      u,v=doubling(x1,x2,y1)
    elif (i>2):
      u,v=point_add(u,x1,v,y1)
  print("k*Pb",u,v)

  x1=ra
  y1=ra
  (e,f)=point_add(u,x1,v,y1)
  print("Pm+k*Pb:",e,f)			#Pm+k*Pb
  
#Decryption
def decrypt(x,y,k,n2,ra,inplen,po1,po2):
 print("*****Decrypting******")
 for i in range(1,k+1):		#kG
  x1=x[ra]
  y1=y[ra]
  if(i==2):
    x2=x1
    l,m=doubling(x1,x2,y1)
  elif (i>2):
    (l,m)=point_add(l,x1,m,y1)
 print("K*G",l,m)

 for i in range(1,n2+1):        #nb*K*G
  x1=l
  y1=m
  if(i==2):
    x2=x1
    s,t=doubling(x1,x2,y1)
  elif (i>2):
    (s,t)=point_add(s,x1,t,y1)
 print("nb*k*G",s,t)

 for i in range(1,n2+1):        #nb*G
  x1=x[ra]
  y1=y[ra]
  if(i==2):
    x2=x1
    g,h=doubling(x1,x2,y1)
  elif (i>2):
    (g,h)=point_add(g,x1,h,y1)
 print("nb*G",g,h)

 for i in range(1,k+1):        #k*nb*G
  x1=g
  y1=h
  if(i==2):
    x2=x1
    (j,o)=doubling(x1,x2,y1)
  elif (i>2):
    (j,o)=point_add(j,x1,o,y1)
 print("k*nb*G",j,o)

 p1=int(s-j)
 p2=int(t-o) 
 print(p1,p2)
 if(p1==p2):
   print("Character Decrypted..")   
 po1.append(p1)
 po2.append(p2)

def decrypt_success(po1,po2,inplen):
 
 lenp=len(po1)
 print(po1,po2)
 #if(lenp==inplen):
  # if(po1==po2):
   #  print("Decrypted Successfully!")
    # print("Original Message:",inp)
   #else:
    # print("Decrypt Failed")

po1=[]
po2=[]
x=[]
y=[]
#inp=input("Enter a Character:")
#inp=inp.replace(' ', '')
inp=""
print("Reading input from text file:")
f = open("demo.txt", "r")
inp=[inp.rstrip('\n') for inp in f]
#inp=input("Enter String:")
inp=inp[0]
inp=inp.replace(' ', '')
print(inp)	
D=int(input("enter D"))
p=int(input("enter a prime number"))
equ(D,p,x,y)
inplen=len(inp)
for i in range(0,inplen):
  inpu=inp[i]
  encode(inpu,0,x,p)


le=len(x)
ran=[]
for i in range(0,le):
  dom=random.randint(0,le)
  ran.append(dom)
n2=2
#k=int(input("enter k"))
#k=random.randint(1,p)
k=3
print("K:",k)
ra=0
start_time = time.time()
for i in range(0,inplen):
  ra=ran[i]
  encrypt(x,y,k,n2,ra)
for i in range(0,inplen):
  ra=ran[i]
  decrypt(x,y,k,n2,ra,inplen,po1,po2)
end_time = time.time()
decrypt_success(po1,po2,inplen)
time=end_time-start_time
print("time taken:",time,"seconds")



