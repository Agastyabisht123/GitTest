def Mul(num1,num2):
  print(int(num1)*int(num2))

def Add(num1,num2):
  print(int(num1)+int(num2))

def Sub(num1,num2):
    print(int(num1)-int(num2))
  
def Div(num1,num2):
    print(int(num1)/int(num2))


num1, num2 = input("Enter two no. separated by , : ").split(",")
Add(num1,num2)
Mul(num1,num2)
Sub(num1,num2)
Div(num1,num2)