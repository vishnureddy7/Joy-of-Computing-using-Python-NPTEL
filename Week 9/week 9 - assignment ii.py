#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs09/progassignment?name=282

import re
print(max(map(int,re.findall(r'[0-9]+',input()))),end="")
