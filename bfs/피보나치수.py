n = int(input())
lst = [0,1]
for i in range(2,n+1):
    m = lst[i-2] + lst[i-1]
    lst.append(m)
print(lst[-1])