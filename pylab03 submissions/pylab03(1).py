# Gully Boy Boht Hard Question

st=input()
node=int(input())
repetation=int(input())

out=st[node:] + st[:node]
re1=out.replace(' ','')*repetation
print(*re1)
