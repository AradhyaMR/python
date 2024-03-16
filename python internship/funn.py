#def my_function():
 #   print("my name is ponnu")
    
#my_function()


#def add_num(a,b):
 #   sum=a+b
  #  return sum
#num1=25
#num2=45
#print("the sum is",add_num(num1,num2))

#def divide_num(c,d):
 #   divide=c/d
  #  return divide
#num1=10
#num2=5
#print("the divide is",divide_num(num1,num2))

#def multiply_num(m,r):
 #   multiply=m*r
  #  return multiply
#num1=2
#num2=4
#print("the multiply is",multiply_num(num1,num2)

    

#def find_square(num):
  #   result=num * num
   #  return result
#square=find_square(3)

#print(square)

# def find_cube(num):
#     result=num * num* num
#     return result
# cube=find_cube(2)

# print(cube)


# def add_numbers(a=7,b=8):
#     sum=a+b
#     print("sum",sum)
#     # add_numbers(2,3)

# add_numbers()

  #keyword argument
# def display_info(first_name, last_name):
#     print('First Name:', First_name)
#     print('Last Name:',last_name)

# display_info(last_name = 'cartman',first_name = 'Eric') 

def find_sum(*numbers):
    result = 0

    for num in numbers:
        result = result + num 

    print("sum = ",result)
find_sum(1,2,3)
find_sum(4,9)
 

