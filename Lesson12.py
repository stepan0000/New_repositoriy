def palindrom(a):
    if a[::1] == a[::-1]:
        print("True")
    else:
        print("False")
stroka = input("Введите строку: ")
palindrom(stroka)