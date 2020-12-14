import math
n = int(input("Nhap vao so n: "));
count = 1;
numb = 2;
while (count < n):
    numb += 1;
    isprime = 1;
    for i in range(2,numb):
        if (numb % i == 0):
            isprime = 0;
            break;
    if (isprime == 1):
        count += 1;
print(numb);
