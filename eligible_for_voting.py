#Q4. Write a program that takes a user's age as input and determines if they are eligible to vote (above 18)

#input section
a=int(input("enter the age of user:"))

#logic section
b=a>=18

#display section
print("person is valid for vote"*b+"person is not valid for vote"*(1-b))