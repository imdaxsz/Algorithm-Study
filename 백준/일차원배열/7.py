n = int(input())
A = []

for i in range(n):
    sum = 0
    avg = 0
    x = input().split(' ')
    high = 0
    low = 0
    for j in range(len(x)):
        if j!=0:
            sum += int(x[j])
    avg = sum/int(x[0])
    for k in range(len(x)):
        if k!=0:
            if int(x[k])>avg:
                high += 1
            else:
                low += 1
    A.append(high/(len(x)-1)*100)
                
for i in range(n):
    print("%.3f"%(A[i])+"%")
