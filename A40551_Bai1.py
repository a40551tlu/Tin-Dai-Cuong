maxN = int(input("Nhap vao so thu nhat: "));
for i  in range(0,4):
    num = int(input("Nhap vao so tiep theo: "));
    if(num > maxN):
        maxN = num;
print("So lon nhat la: ", maxN)
