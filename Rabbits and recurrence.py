# program to calculate total number of rabbit pairs present after n months, 
# if each generation, every pair of reproduction-age rabbits produces k rabbit pairs, instead of only one.
# variation of fibonacci sequence

# n = number of months
# k = number of rabbit pairs

# recursive function for calculating growth in rabbit population
def rabbits(n, k):
    if n <= 1:
        return n
    else:
        return rabbits(n - 1, k) + k * rabbits(n - 2, k)
        

# prints the total number of rabbit pairs each month.
for x in range(1, 8):
    print (f"Total number of rabbit pairs after {x} months: ", (rabbits(x, 3)))



