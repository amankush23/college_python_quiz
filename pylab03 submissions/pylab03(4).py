# Binary string with consecutive 1’s

width=int(input())
count = 0
for i in range(2**width):
    if '11' in bin(i):
        count+=1
print(count)