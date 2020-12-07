a = int(input("nhap nam: "))

if ((a % 100) == 0) and ((a % 400) == 0):
  print(a, " la nam nhuan.")
else:
  if ((a % 4 == 0) and (a % 100 != 0)):
    print(a," la nam nhuan.")
  else:
    print(a, "khong la nam nhuan")
