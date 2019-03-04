#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs09/progassignment?name=267

r,c=map(int,input().split());
x=1
for i in range(r):
  for j in range(c-1):
    print(x,end=" ");
    x+=1
  print(x);
  x+=1;
