#link for the question
#https://onlinecourses.nptel.ac.in/noc19_cs09/progassignment?name=291

s=input();
n=0;
tw='ADOPQR'
th='B'
for i in s:
  if(i in tw):
    n+=1;
  elif(i in th):
    n+=2;
print(n,end='');
