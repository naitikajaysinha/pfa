def even_check(n):
    if n%2==0:
        print("Even number")
    else:
        print("Odd number")

def factor_list(n):
    temp=[]
    for i in range(1,n):
        if n%i==0:
            temp.append(i)
        print(temp)

