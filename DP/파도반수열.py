n = int(input())

for i in range(n):
    m= int(input())


    if m >=3:
        lst = [1,1,1]
        for j in range(3,m):
            num = lst[j-3] + lst[j-2]

            lst.append(num)
            print(lst)
        print(lst[m-1])
    else:
        print(1)
