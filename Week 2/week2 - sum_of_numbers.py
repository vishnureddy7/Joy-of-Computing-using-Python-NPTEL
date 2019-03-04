def sum_of_elements(a):
    s = 0;
    for i in a:
        s += i;
    return s;
n = int(input("Enter the total number of elements? "));
a = [];
i = 0;
print("Enter the elements: ",end='');
while(i<n):
    s = input().split();
    for j in s:
        if(i>=n):
            break;
        a.append(int(j));
        i += 1;
print('Sum of all given elements: ',sum_of_elements(a));
