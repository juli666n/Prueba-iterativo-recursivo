def rec(n):
    global num
    print (n)
    if n == 1:
        return
    elif imp != 0:
        return rec(3 * n + 1)
    else:
        return rec(n / 2)


num = input("ingrese numero:\n")
imp = num % 2
rec(num)
