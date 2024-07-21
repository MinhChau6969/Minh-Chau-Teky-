a=float(input("Hay nhap can nang cua ban (kg):"))
b=float(input("Hay nhap chieu cao cua ban (m):"))
if a<0 or b<0:
    print("Error")
else:
    w=a/b**2
    if w>40:
        print("Beo phi cap do 3")
    elif w>=35:
        print("Beo phi cap do 2")
    elif w>=30:
        print("Beo phi cap do 1")
    elif w>=25:
        print("Thua can")
    elif w>=18.5:
        print("Binh thuong")
    elif w>=17:
        print("Gay cap do 1")
    elif w>=16:
        print("Gay cap do 2")
    else:
        print("Gay cap do 3")