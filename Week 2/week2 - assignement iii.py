#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs09/progassignment?name=261

n=int(input());
a=list(map(int,input().split()));
for i in range(n-1):
  print(a[i]+a[-i-1],end=" ");
print(a[0]+a[-1],end="");
