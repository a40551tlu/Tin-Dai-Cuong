n = int(input("Nhap vao so n: "));
for i in range(1, n+1):
    tonguoc = 0;
    for j in range(1, i):
        if (i % j == 0):
            tonguoc += j;
    if tonguoc == i:
        print(i, ' ');
