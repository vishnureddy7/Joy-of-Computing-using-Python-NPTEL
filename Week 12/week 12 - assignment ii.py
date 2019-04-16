#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs09/progassignment?name=290

s=list(input());
n=len(s);
#first replace dots
for i in range(n):
    if(s[i]=='.'):
        s[i]=s[n-i-1];
s=''.join(s);
s=s.replace('.','a');
#check if the string is palindrome
print(''.join(s) if s==s[-1::-1] else -1,end='');
