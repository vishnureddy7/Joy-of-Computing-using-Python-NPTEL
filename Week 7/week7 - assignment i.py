#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs09/progassignment?name=275

n=int(input());
a=[list(map(int,input().split())) for i in range(n)];
for i in range(n):
  for j in range(n):
    end = '' if j == n-1 else ' ';
    if(i<=j):
      print(a[i][j], end=end);
    else:
      print(0, end=end);
  end = '' if i == n-1 else '\n';
  print('',end=end);
