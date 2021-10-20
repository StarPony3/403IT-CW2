'''
lst = [2, 5, 47, 2, 90, 100, 5]

def insertion_sort(lst):
    for x in range(len(lst)):
        current_item = lst[x]
        y = x

        while y > 0 and lst[y - 1] > current_item:
            lst[y] = lst[y - 1]
            y = y - 1

        lst[y] = current_item
        print (lst)
        
        

print (insertion_sort(lst))
print (lst)

n = 11 #replace input                                                                        
m = 3 #replace input                                                                       
bunnies = [1, 1]                                                               
months = 2
count = []                                                                     
while months < n:                                                              
    if months < m:                                                             
        bunnies.append(bunnies[-2] + bunnies[-1])                              
    elif months == m or count == m + 1:                                        
        bunnies.append(bunnies[-2] + bunnies[-1] - 1)                          
    else:                                                                      
        bunnies.append(bunnies[-2] + bunnies[-1] - bunnies[-(                  
            m + 1)])                                                           
    months += 1                                                               
    print(bunnies[-1])

'''
dead_rabbits = 0
def rabbits(t, m):
    if m < 3:
        if t <= 1:
            return t
        else:
            return rabbits(t - 1, m) + rabbits(t - 2, m)
    #else: 
    #    if t <= 1:
    #        return t
    #    else:
    #        return (rabbits(t - 1, m) + (rabbits(t - 2, m)) - (m  + 1))

for t in range(1, 11):
    print (rabbits(t, 3))