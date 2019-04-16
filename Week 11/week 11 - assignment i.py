#link for the question
#https://onlinecourses.nptel.ac.in/noc19_cs09/progassignment?name=287

n,m=map(int,input().split());
s=sorted(list(map(int,input().split())));
mini=s[-1]-s[0];
for i in range(n-m+1):
  if(s[i+m-1]-s[i]<mini):
    mini=s[i+m-1]-s[i];
print(mini,end="");
