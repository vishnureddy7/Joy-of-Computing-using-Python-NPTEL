def sum_upto_n(n):
    s = 0;
    for i in range(1,n+1):
        s += i;
    return s;

n = int(input('Enter n value? '));
print('Sum of numbers upto',n,'is',sum_upto_n(n));
