#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs09/progassignment?name=279

s=input();
d={}
for i in s:
  if(i.isalpha()):
    i=i.lower();
    try:
      d[i]+=1;
    except:
      d[i]=1;
print('YES' if len(d.keys())==26 else 'NO',end='');
