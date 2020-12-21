n = int(input("Nhap vao n: "))
result = 0;
for i in range(1,n + 1):
    result += 1/(i*(i+1));
print(result);
