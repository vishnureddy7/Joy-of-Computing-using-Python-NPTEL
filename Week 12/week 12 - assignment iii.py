#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs09/progassignment?name=292

s=input();
u,l=0,0
for i in s:
    if(i.islower()):
        l+=1;
    elif(i.isupper()):
        u+=1;
print(u,l,end='');
