#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs09/progassignment?name=281
n=int(input());
a=[];
for i in range(n):
  a.append(list(map(int,input().split())));
di='d';
l,r,u,d=0,n-1,0,n-1
s=[];
while(True):
  if(di=='d'):
    if(u>d):
      break;
    for i in range(u,d+1):
      s.append(a[i][l]);
    l=l+1;
    di='r';
  elif(di=='r'):
    if(l>r):
      break;
    for i in range(l,r+1):
      s.append(a[d][i]);
    d=d-1;
    di='u';
  elif(di=='u'):
    if(u>d):
      break;
    for i in range(d,u-1,-1):
      s.append(a[i][r]);
    r=r-1;
    di='l';
  else:
    if(l>r):
      break;
    for i in range(r,l-1,-1):
      s.append(a[u][i]);
    di='d';
    u=u+1;
print(' '.join(map(str,s)),end='');
