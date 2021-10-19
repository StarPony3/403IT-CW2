while True:

    input_mark = int(input("Enter raw mark: "))

    def classification(input_mark):

        if input_mark < 40:
            return (f"{input_mark}: Fail")
        elif input_mark >= 40 and input_mark < 50:
            return (f"{input_mark}: 3rd")
        elif input_mark >= 50 and input_mark < 60:
            return (f"{input_mark}: 2.2")
        elif input_mark >= 60 and input_mark < 70:
            return (f"{input_mark}: 2.1")
        else:
            return (f"{input_mark}: 1st")

    print (classification(input_mark))