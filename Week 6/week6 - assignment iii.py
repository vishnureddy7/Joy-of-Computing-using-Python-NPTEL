#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs09/progassignment?name=274

def printDict():
  x=int(input())
  d={}
  for i in range(1,x+1):
    d[i]=i**2
  print(d,end='')
printDict()
