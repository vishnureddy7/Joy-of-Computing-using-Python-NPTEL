#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs09/progassignment?name=280

vowels = 'aeiou'
s=input();
i=0;
n=len(s);
while(i<n):
  print(s[i],end='');
  if(s[i] in vowels):
    while(i<n and s[i] in vowels):
      i+=1;
    continue;
  i+=1;
