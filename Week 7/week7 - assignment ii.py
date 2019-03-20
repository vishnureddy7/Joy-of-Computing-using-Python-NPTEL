#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs09/progassignment?name=276

n=int(input());
a=[list(map(int,input().split())) for i in range(n)];
i=0;
sym='YES';
while(i<n-1):
  j=i+1;
  while(j<n):
    if(a[i][j]!=a[j][i]):
      sym='NO';
      break;
    j+=1;
  i+=1;
print(sym,end='');
