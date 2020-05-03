"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Give some direction/instructions to the user an the list of valid operations

print("""\nAn equation is represented by an operation followed by 1 or 2 
        numbers, all separated by a single space. Example:
    + 2 3 --> Answer = 5 or,
    pow 2 3 --> Answer = 8,
    cube 3 --> Answer = 27, etc.\n""")

print("Enter q to quit.\n\nList of valid operations are: \n +, -, *, /, square, cube, pow, mod\n")


list_of_operations = []
list_of_operations = ["+", "-", "*", "/", "square", "cube", "pow", "mod"]
 
# for operation_type in list_of_operations:   # Loop thorugh and print the valid 
#     print(f"{operation_type}, ")             # operations  
                                            
# print ("\n")                                # Print a blank line for a 
#                                             # cognitive breather :)


user_input = ""
index_counter = 0
operator = ""

while user_input != 'q':
    user_input = input("Enter your equation > ")
    tokenized_user_input = user_input.split(" ")
    
    operator = tokenized_user_input[0]  


    if (operator == "q"):
        break
    else:     
        try:
        
            # If user enters a valid operator and 2 other values
            # Extract the values from list and continue processing 
        
            if ((len(tokenized_user_input) == 3) and
                (operator in list_of_operations)):
   
                value_1 = float(tokenized_user_input[1])
                value_2 = float(tokenized_user_input[2])

                # Conditions to check for the operator, perform the operation
                # on the values entered and print the result in a readable format.

                if operator == list_of_operations [0]:  
                    return_value = add(value_1, value_2)
                    print (f"The sum is {return_value}.\n")

                elif operator == list_of_operations [1]:
                    return_value = subtract(value_1, value_2)
                    print (f"The difference is {return_value}.\n")


                elif operator == list_of_operations [2]:
                    return_value = multiply(value_1, value_2)
                    print (f"The product is {return_value}.\n")


                elif operator == list_of_operations [3]:
                    return_value = divide(value_1, value_2)  
                    print (f"The result is {return_value}.\n")


                elif operator == list_of_operations [7]:
                    return_value = mod(value_1, value_2)  
                    print (f"The mod is {return_value}.\n")

                # If it's a valid operator, but wrong number of values 
                # for the operation, display an error message

                else:
                    print(f"Operation '{operator}' cannot be done on " + 
                    f"{value_1} and {value_2}. Please try again.\n")

                 

            # User enters a valid operator and only one value, then extract that
            # value and continue processing

            elif ((len(tokenized_user_input) == 2) and 
              (operator in list_of_operations)):
            
                value_1 = float(tokenized_user_input[1])
        
                # Check operations are valid and display the computed result
                # else, display a detailed error message 

                if operator == list_of_operations [4]:
                    return_value = square(value_1)
                    print (f"The square is {return_value}.\n")

                elif operator == list_of_operations [5]:
                    return_value = cube(value_1)
                    print (f"The cube is {return_value}.\n")


                else:
                    print(f"Operation '{operator}' cannot be done on {value_1}"
                    + f" and {value_2}. Please try again.\n")
                    break
      
            # If the first value specified is not a valid operation
            else:
                print(f"The value entered '{operator}' is not valid." +
                f" See the list of valid operations above and try again.\n")
                
        # If any of the above results in any error, then go through this exception
        except ValueError:
                print("Hmm...Something was not right!!")
                break
    

        