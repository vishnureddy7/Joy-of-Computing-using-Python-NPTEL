def multiplication_table(n,k=10):
    print('Multiplication for',n);
    print('-'*20);
    for i in range(1,k+1):
        print('%2d X %2d = %3d'%(n,i,n*i));

n = int(input('Enter the number for multiplication table '));
multiplication_table(n)
