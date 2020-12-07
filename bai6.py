n = int(input("Nhap so n: "))
i = 1
count = 1
while (i != n):
  if (n % i == 0):
    count += 1
  i += 1
print(count)
