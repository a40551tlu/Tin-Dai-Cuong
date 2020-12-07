a = int(input("Nhap vao thang: "))
b = int(input("Nhap vao nam: "))
if a == 2:
  if ((b % 100) == 0) and ((b % 400) == 0):
    print("Co 29 ngay.")
  else:
    if ((b % 4 == 0) and (b % 100 != 0)):
      print("co 29 ngay.")
    else:
      print("Co 28 ngay.")
elif a in [1,3,5,7,8,10,12] :
  print("Thang co 31 ngay.")
else :
  print("Thang co 30 ngay")
