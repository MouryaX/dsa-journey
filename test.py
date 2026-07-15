# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=arr[0]>>1
    print(ans)
    c=1
    for i in range(1,n):
        while arr[i]> ans:
            arr[i]=arr[i]>>1
            c+=1
    print(c)