#simple calculator 
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    if b==0:
        return"cant divide by zero"
    return a/b

print("simple calculator")
print("1.add")
print("2.sub")
print("3.mult")
print("4.div")

select = input("enter which operation you want to perform(1-4)")
num1= float(input("enter first nummber"))
num2 =float(input("enter second number"))
if select =="1":
    print("result",add(num1,num2))
elif select =="2":
    print("result",sub(num1,num2))
elif select =="3":
    print("result",mult(num1,num2))
elif select =="4":
    print("result",div(num1,num2))
else:
    print("no valid choice")