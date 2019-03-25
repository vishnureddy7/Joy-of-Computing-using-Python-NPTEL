#link for the question
#https://onlinecourses.nptel.ac.in/noc19_cs09/progassignment?name=278

s=map(int,input().split());
d={};
for i in s:
  try:
    d[i]+=1;
  except:
    print(i,end=' ');
    d[i]=1;
