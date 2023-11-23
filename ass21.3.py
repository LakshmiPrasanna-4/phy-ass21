# Write a program to print elements in order within a specified interval in descending order.

n=int(input())
l=list(map(int,input().split()))
s,e=map(int,input().split())
bs=l[0:s]
afs=l[e+1:n]
sr=l[s:e+1]
sr.sort(reverse=True)
res=bs+sr+afs
for i in res:
    print(i,end=' ')
