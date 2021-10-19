# program to retrieve a student's mark from a dictionary and convert
# it to a percentage and grade

# dictionary of student name and mark
mark_dict = {'bob':'50', 'alice': '60', 'molly':'30', 'fred':'75', 'george':'10', 'ron':'85', 'arthur': '0'}

# total marks available
total_mark = 90

# takes user's name and matches it with dict keys
def name_validation():
        
        # takes name
        name_input = input("Enter first name: ")
        # converts input to match dict keys
        name_input = name_input.lower()

        # validates name
        if name_input not in mark_dict:
            print ("Name not found. Please check input")
            return name_validation()
        # returns user's grade if name valid
        else:
            return percentage_calculator(name_input)


# calculates user's grade and takes output of another function as an argument.
def percentage_calculator(name_input):
        
        # calculates percentage
        mark = int(mark_dict[name_input])
        percentage = (mark / total_mark) * 100
        

        # returns grade to user
        print (f"Mark: {mark}")
        print (f"Percentage: {percentage}%")
        if percentage >= 40:
            return ("Pass")
        else:
            return ("Fail")
    

print (name_validation())

