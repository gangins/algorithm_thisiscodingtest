N = int(input())
lst =[]
for i in range(N):

    lst.append(map(int,input().split()))
lst.sort(reverse=True)

print(lst[4])

