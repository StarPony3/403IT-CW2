# program for OR gate
while True:

    # applies Boolean operator 'OR' and returns Boolean value
    def or_gate (a, b):
        if a == '1' and b == '1':
            return True
        elif a == '1' and b == '0':
            return True
        elif a == '0'  and b == '1':
            return True
        else:
            return False

    # two inputs taken from user.
    # loop breaks if either invalid.
    input_1 = input ("Enter 0 or 1. Press any other key to exit.")

    if input_1 != '1' and input_1 != '0':
        break

    input_2 = input ("Enter 0 or 1. Press any other key to exit.")

    if input_2 != '1' and input_2 != '0':
        break

    # calls function and passes both inputs as arguments
    print (or_gate(input_1, input_2))

