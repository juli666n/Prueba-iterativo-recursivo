n = input("ingrese numero:\n")
imp = n % 2
while True:
    print (n)
    if n == 1:
        break
    elif imp != 0:
        n = 3 * n + 1
    else:
        n = n / 2
