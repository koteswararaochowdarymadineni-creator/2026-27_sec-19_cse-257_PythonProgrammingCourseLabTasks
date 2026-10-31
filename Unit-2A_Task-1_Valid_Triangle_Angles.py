a =int(input("Enter the first angle in degrees :"))
b =int(input("Enter the second angle in degrees :"))
c =int(input("Enter the third angle in degrees :"))
if a>0 and b>0 and c>0 and a+b+c==180:
    print(f"valid triangles (angle= {a},{b},{c})")
else:
    print(f"Not valid triangles (angle= {a},{b},{c})")