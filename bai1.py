a = int(input("nhap nam: "))
if (a < 100) and (a % 4 == 0):
	print(a, "la nam nhuan")
elif ((a % 4 == 0) and (a % 100 != 0)):
  print(a, " la nam nhuan.")
else:
  print(a, " khong la nam nhuan.")
