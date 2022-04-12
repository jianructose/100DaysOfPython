from art import logo
# print(logo)



# Calculator
# add
def add(n1, n2):
  return n1+n2

# subtract
def subtract(n1, n2):
  return n1-n2

# multiply
def multiply(n1, n2):
  return n1*n2

# divide
def divide(n1, n2):
  return n1/n2

operations = {
  "+":add, 
  "-":subtract,
  "*":multiply,
  "/":divide,
}

def calculate():
  print(logo)
  end_flag = False
  num1 = float(input("first number?: \n"))
  for k in operations:
      print(k)  
  while not end_flag: 
    op = input("Which operation? :\n")
    func = operations[op]
    num2 = float(input("next number?: \n"))
    res = round(func(num1, num2), 4)
    
    print(f"{num1} {op} {num2} = {res}")
    keep = input(f"Type 'y' to continue calculating with {res}, or type 'n' to reset a new round of calculation.[y]:\n")
    
    if keep == "y":
      num1 = res
      
    else:
      end_flag = False
      # call function again and reset, recursion 
      calculate()

calculate()