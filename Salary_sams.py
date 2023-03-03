a=int(input("Enter x/yth part of sam's weekly salary : "))
x,y = map(int,input("enter x,y seperated by comma(,) : ").split(","))
z=int(input("Enetr value of n to get 1/nth part of sam's weekly salary : "))
print("1/nth part of sam's salary is",(a*y)/(z*x))
