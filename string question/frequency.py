# st=input("enter the string:")
# ch=input("enter the character:")

# count=0

# for a in st:
#       if a == ch:
#         count+=1
# print(count)

# chr=input("enter the character:")
# reg = ""
# for x in chr:
#   count=0
#   if x not in reg:
      
#       for a in chr:
#           if a==x:
#             count+=1
#       print(x,':',count)
#       reg+=x


st=input("enter the character:")
reg=""
count=0
for ch in st:
    if ch not in reg:
        count+=st.count(ch)
        print(f'({ch}:{count})')
        reg+=1

