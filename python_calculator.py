#!/usr/bin/env python
# coding: utf-8

# In[1]:


myfile=open("file.txt","r")
print(myfile.read())


# In[2]:


myfile=open("file.txt","w")
myfile.write("output is :")


# In[3]:


myfile=open("file.txt","r")
print(myfile.read())


# In[4]:



def add(x,y):
  return x+y
def subtract(x,y):
  return x-y
def multiply(x,y):
  return x*y
def divide(x,y):
  return x/y
print("select operation:")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
while True:
  choice=input("enter the choice (1/2/3/4):")
  num1=float(input("enter the first number:"))
  num2=float(input("enter the second number:"))
  if choice=='1':

   print(num1,"+", num2,'=',add(num1,num2))
   myfile=open("file.txt","r+")
   myfile.read()
   myfile.write("add(num1,num2 ))")
  if choice=='2':
    x=print(num1 ,"-", num2,'=',subtract (num1,num2))
    myfile=open("file.txt","r+")
    myfile.read()
    myfile.write("num1-num2")
  if choice=='3':
    print(num1, "*" ,num2,'=',multiply(num1,num2))
    myfile=open("file.txt","r+")
    myfile.read()
    myfile.write("multiply(num1,num2))")
  if choice=='4':
    print(num1 ,"/" ,num2, '=',divide(num1,num2))
    myfile=open("file.txt","r+")
    myfile.read()
    myfile.write("divide(num1,num2))")
  next_calculation=input("lets do next next one? (y/n):")
  if next_calculation =="n":
    break

else:
  print("invalid")


# In[5]:


myfile=open("file.txt","r+")
print(myfile.read())


# In[6]:


myfile=open("file.txt","r+")
print(myfile.read())


# In[8]:


myfile=open("file.txt","r")
print(myfile.read())


# In[ ]:




