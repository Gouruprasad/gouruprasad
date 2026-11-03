nums = [-1,-99,-111111111,0.1, 3,56,78,101,745,8494,2.00001]

#we remove number that is less than 0

save = [] #we create a empty lsit to store the num we need

for i in nums: # using for loop cause we know the iterations
    if i >= 0:
       save.append(i) #storing it in the new list "save"
print(save)
