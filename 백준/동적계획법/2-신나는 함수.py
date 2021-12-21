import sys
input=sys.stdin.readline

ans = [[[0 for i in range(21)] for j in range(21)] for k in range(21)]

for i in range(21):
    for j in range(21):
            for k in range(21):
                if i==0 or j==0 or k==0:
                    ans[i][j][k] = 1
                elif i < j and j < k:
                    ans[i][j][k] = ans[i][j][k-1]+ans[i][j-1][k-1]-ans[i][j-1][k]
                else:
                    ans[i][j][k] = ans[i-1][j][k]+ans[i-1][j-1][k]+ans[i-1][j][k-1]-ans[i-1][j-1][k-1]

while(True):
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break;          
    if a < 1 or b < 1 or c < 1:
        print("w(%d, %d, %d) = %d" %(a, b, c, ans[0][0][0]))   
    elif a > 20 or b > 20 or c > 20:
        print("w(%d, %d, %d) = %d" %(a, b, c, ans[20][20][20]))

    else:
        print("w(%d, %d, %d) = %d" %(a, b, c, ans[a][b][c]))
    
