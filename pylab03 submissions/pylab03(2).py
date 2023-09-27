# Adjacent characters

st=input()
l=len(st)
s=""
t=0
if len(st)%2 !=0:
    print("Odd length.")

else:
    for i in range(0,l,2):
        s+=st[i+1]+st[i]
print(s)