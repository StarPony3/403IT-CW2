# program for NOT gate
while True: 

    # applies Boolean operator 'NOT' and returns Boolean value
    def not_gate (a):
        if a == '1':
            return False
        else:
            return True

    # takes input from user    
    Input = input ("Enter 1 or 0. Press any other key to exit.")
    
    # checks input using Boolean comparison operators
    # breaks loop if input invalid
    if Input != '1' and Input != '0':
        break
 
    # calls function and passes user input as argument
    print (not_gate (Input))
    
    
