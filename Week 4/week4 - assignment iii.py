#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs09/progassignment?name=268

from random import randint

def issorted(a):
  for i in range(1,n):
    if(a[i-1]>a[i]):
      return False;
  return True;

n=int(input());
a=[]
for i in range(n):
  a.append(int(input()))
while(not issorted(a)):
  i=randint(0,n-1);
  j=randint(0,n-1);
  a[i],a[j]=a[j],a[i]
print(" ".join(map(str,a)),end="");
