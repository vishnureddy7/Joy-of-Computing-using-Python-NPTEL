#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs09/progassignment?name=265

x,y=0,0;
for i in input():
  if(i=='1'):
    x+=1;
  else:
    y+=1;
print("YES" if x==1 or y==1 else "NO",end="");
