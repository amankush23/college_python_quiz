#Q2 Develop a temperature converter program that converts between Celsius, Fahrenheit, and kelvin.

#input section

celcius=int(input("enter the temperature"))

#logic section
fahrenheit=((9//5)*(celcius))+32
kelvin=273+celcius

#display section
print("c",celcius,"f",fahrenheit,"k",kelvin)


