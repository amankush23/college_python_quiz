# pattern char 'A'

rows=int(input())
l=int(input())
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ",end="")
    for j in range(2*i-1):
        if j==0 or j==2*i-2 or  i==l:
             print("*",end="")
        else:
            print(" ",end="")
    print()
        