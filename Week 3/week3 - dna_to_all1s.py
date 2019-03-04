import random
def all_ones(dna):
    for bit in dna:
        if(bit=='0'):
            return False;
    return True;

#total number of bits in dna
n = random.randint(50,200);
ones = random.randint(0,n);
zeros = n - ones;
dna = random.sample('0'*zeros + '1'*ones,n);
print('DNA is ',str(dna));
it = 0;
while(True):
    pos = random.randint(0,n-1);
    if(dna[pos]=='0'):
        dna[pos] = '1';
    it += 1;
    if(all_ones(dna)):
        break;
print("DNA all converted 1's is ",str(dna));
print('Number of iterations to make all ones ',it);
