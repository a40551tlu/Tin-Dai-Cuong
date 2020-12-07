n = int(input("Nhap n:"))
maxN = float(input("Nhap vao so thu 1:"))
i = 1
while (i < n):
  num = float(input("nhap so: "))
  if num > maxN:
    maxN = num
  i = i + 1
print("So lon nhat la: ", maxN)
