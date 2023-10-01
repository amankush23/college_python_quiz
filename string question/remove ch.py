ch=input("enter the character:")
s=''
for i in ch:
    if "a" <= i <= "z" or "A" <= i <= "Z":
        print(i,end="")
    else:
        print(s,end="")


