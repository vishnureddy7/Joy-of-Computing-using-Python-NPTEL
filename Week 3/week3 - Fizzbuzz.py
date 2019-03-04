n = int(input('Enter n value? '));
for i in range(1,n+1):
    if(i%3==0):
        print('fizzbuzz' if i%5==0 else 'fizz');
    else:
        print('buzz' if i%5==0 else i);
