# celsius to fahrenheit

c = input("Enter temp in celsius : ")

c = float(c)

f = (c*9/5) + 32

print('Fahrenheit : ',f)



# fahrenheit to celsius

f = input("Enter temp in fahrenheit : ")

f = float(f)

c = (f-32)*5/9

print('Celsius : ',c)


# Simple Interest calculator
#formula : (primary Amount * Time  * interest rate)/100

p = input("Enter primary amount : ")
n = input("Enter time duration : ")
r = input("Enter interest rate : ")

p = int(p)
n =int(n)
r = int(r)

si = (p*n*r)/100
print("Simple Interest is : ",si)