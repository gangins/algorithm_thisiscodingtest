N,K = map(int,input().split())
count = 0
for i in range(N):
    if N > 1:
        if N % K ==0:
            N /= K
            count +=1

        else:
            N -=1
            count += 1
    else: break
print(count)