#link for question
#https://onlinecourses.nptel.ac.in/noc19_cs09/progassignment?name=270

def endsort(a): 
  sa = sorted(a) 
  n = len(a)
  k = 0
  for i in range(n):
    try:
      k = a.index(sa[i], k)+1 
    except ValueError:
      break 
  else:
    i += 1;
  return n-i;

print(endsort(list(map(int, input().split()))),end="");
