#Author - Satyam Ramawat 
import sys

n=input("Enter the size of array")
m=input("Enter the searching element")
list=input("please input 5 value")
for i in range(1,n):
  if (m in list): 
   print("value found")
   break
  else:
   print("value is not there") 