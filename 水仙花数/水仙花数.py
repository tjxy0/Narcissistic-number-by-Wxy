for i in range(101,1000):
    if (i//10%10) ** 3 + (i//100) ** 3 + (i%10) ** 3 == i:
        print(i)
    else:
        print("NO",end=" ")
