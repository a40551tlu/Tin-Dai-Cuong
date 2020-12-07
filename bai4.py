a = int(input("Nhap so a: "))
hangnghin = int(a / 1000)
hangdv = int(a % 10)
hangtram = int(a / 100) % 10
hangchuc = int(a / 10) % 10
if(hangnghin == hangdv) and (hangtram == hangchuc):
  print("La so doi xung")
else:
  print("Khong la so doi xung")
