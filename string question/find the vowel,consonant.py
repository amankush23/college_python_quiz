# str=input()
# count=0
# reg=""
# v="aeiouAEIOU"

# for i in str:
#    if i not in reg:
#      if i in v:
#         if i not in reg:
#             count+=1
#             print(f'Vowel=  {i}:{count}')
#             reg+=i
# for "a"<=i<="z" or "A"<=i<="Z":
# if i not in reg:
#             count+=1
#             print(f'consonant=  {i}:{count}')
#             reg+=i

#             st=input("enter the character:")
# reg=""
# for ch in st:
#     if ch not in reg:
#         count=st.count(ch)
#         print(f'{ch}:{count}')
#         reg+=1


st=input("enter the string:")
alp_u=0
alp_l=0
digits=0
cons=0
vow=0
special=0

for i in st:
    if i in "aeiouAEIOU":
        vow +=1
    elif 'a' <= i <= 'z':
        alp_l +=1
        cons+=1
    elif 'A' <= i <= 'Z':
        alp_u +=1
    elif '0' <= i <= '9':
        digits +=1
    else:
        special+=1

print(f'{"Number of Alphabets_Upper_case":30}:{alp_u}')
print(f'{"Number of Alphabets_Lower_case":30}:{alp_l}')
print(f'{"Number of Digits":30}:{digits}')
print(f'{"Number of Vowels":30}:{vow}')
print(f'{"Number of consonants":30}:{cons}')
print(f'{"Number of Special characters":30}:{special}')

 

    
    