def fib(n):

    a = 0
    b = 1
    print(a, 1)



    if n == 1:
        pass
    elif n == 2:
        print(b, 2)



    print(b, 2)
    for i in range(3, n):
        c = a + b
        a = b
        b = c
        print(c, i)


n = int(input("Enter the number of fibbonaci sequence you want: "))

fib(n + 1)
