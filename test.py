n = 5
lost = [4, 2]
reserve = [3, 5]

lost.sort()
reserve.sort()

reserve_set = [set(reserve) - set(lost)]
lost_set = [set(lost) - set(reserve)]

num = [0]*n

for i in range(len(reserve_set)):
    num[reserve_set[i]-1] = 100

answer = 0
cnt = 0
for i in range(len(lost_set)):
    for j in range(len(reserve_set)):
        if ((int(lost_set[i])-1) or (int(lost_set[i])+1)) == int(reserve_set[j]):
            k=lost_set[i]
            reserve_set[j] = 100
            num[k-1] = 100
            lost_set[i] = 100
            break
        else:
            continue

for i in range(len(num)):
    if num[i]==100:
        cnt += 1

print(cnt+(n-len(lost_set)-len(reserve_set)))

# answer = cnt
# if cnt > n:
#     print(n)
# print(answer)