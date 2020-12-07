a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
c = int(input("Nhap so c: "))

if a == 0:
  if b == 0:
    print("Phuong trinh vo nghiem. \n")
  else :
    if c == 0:
    print("Phuong trinh co vo so nghiem ")
  else :
      print("Phuong trinh co nghiem la: ", -c / b)
else :
  delta = b*b - 4*a*c
  if delta < 0:
    print("Phuong trinh vo nghiem")
  elif delta > 0:
    print("Phuong trinh co 2 nghiem phan biet x1, x2 la:",(-b+sqrt(delta))/2*a,' ', (-b-sqrt(delta))/2*a)
  else :
    print("Phuong trinh co nghiem kep la:", -b/2a)
