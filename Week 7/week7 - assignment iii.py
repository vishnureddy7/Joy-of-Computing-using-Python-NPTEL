#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs09/progassignment?name=277

m,n=map(int,input().split())
a=[list(map(int,input().split())) for i in range(m)];
b='YES';
for i in range(m):
  for j in range(n):
    if(a[i][j]!=0 and a[i][j]!=1):
      b='NO';
      break;
  if(b=='NO'):
    break;
print(b,end='')
