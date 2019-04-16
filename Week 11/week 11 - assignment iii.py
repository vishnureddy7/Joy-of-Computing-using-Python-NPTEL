#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs09/progassignment?name=289
s = list(input().split());
r = [];
z = 0;
for i in s:
    if(i=='0'):
        z += 1;
        continue;
    r.append(i);
r = r + ['0'] * z;
print(' '.join(r),end='');
