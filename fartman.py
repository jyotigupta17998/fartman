def start():
    print("1.for no argument no return type")
    print("2.for with argument no return type")
    print("3.for no argument with return type ")
    print("4.for with argument with trurn type")

    n=int(input("enter the option type:"))
    if n==1:
        def sum():# no argument no return type
            n=int(input("enter the 1st no.="))
            m=int(input("enter the 2nd no.="))
            print(n+m)
        sum()
    start()
    elif n==2:
        def sum(n,m): # with argument no return type
            s=n-m
            print(s)
        n=int(input("enter the 1st no.="))
        m=int(input("enter the 2nd no.="))
        sum(n,m)
    start()
    else:
        print("Please enter valid no.")
        start()
start()