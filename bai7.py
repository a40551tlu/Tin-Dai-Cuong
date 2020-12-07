# your code goes here
n = int(input("Nhap so n: "))
i = 2
nt = 1
while (i != n-1):
  if (n % i == 0):
    nt = 0
  i += 1
if nt == 0:
	print("Khong la so nguyen to")
else:
	print("La so nguyen to")
