x = int(input("Nhap vao so x: "));
n = int(input("Nhap vao so n: "))
ketqua = 0;
i = 1;
tuSo = 1;
mauSo = 1;
while (i <= n):
    tuSo = tuSo * x;
    mauSo = mauSo * i;
    ketqua = ketqua + tuSo/mauSo;
    i += 1;
print(int(ketqua));
