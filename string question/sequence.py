st=int(input("enter the number:"))
n=int(input("enter the number:"))
s=''
print(st)
while n:
    reg=''
    for ch in st:
        if ch not in reg:
            ft=f'{st.count(ch)}{ch}'
            s+=ft
            reg+=ch
    print(s)
    n-=1
    st=s
    s='' 


        