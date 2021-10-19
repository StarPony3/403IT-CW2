# program for AND gate
while True:

     # applies Boolean operator 'AND' and returns Boolean value
    def and_gate (a, b):
        if a == '1' and b == '1':             
            return True        
        else:
            return False

    # takes two inputs from user
    # loop breaks if either input invalid
    input_1 = input("Enter 1 or 0. Press any other key to exit.")

    if input_1 != '1' and input_1 != '0':
       break

    input_2 = input("Enter 1 or 0. Press any other key to exit.")
    
    if input_2 != '1' and input_2 != '0':
        break
    
    # # calls function and passes both user inputs as argument
    print (and_gate (input_1, input_2))


   
   
   
 
 
 
