####################################################################################### 
###                     Youssef Ibrahim 151912                                      ###
###                         IT 210 Project                                          ###
###     Question 4  Memory Allocation Methods-Fixed Partition a) First Fit          ###
#######################################################################################


# The below code creates two variables bnum and pnum and assigns them integer values returned by the int() function. 
# The input() function takes input from the user and the int() function converts the input to an integer.
bnum = int(input("How many blocks:\t"))
pnum = int(input("How many processes:\t"))

# The below code creates two empty lists bnlist and pnlist. 
# These lists will be used to store the block sizes and process sizes.
bnlist = []
pnlist = []

# The below code uses a for loop to iterate over the range from 0 to bnum. 
# Inside the loop, the input() function is used to get input from the user and convert it to an integer using the int() function. 
# The integer value is then added to the bnlist list using the append() method.
# This integer value represents block number "i" our of a total of "bnum" blocks.
for i in range(bnum):
    bsize = int(input(f"Enter block size for block number {i + 1}:\t"))
    bnlist.append(bsize)

# The below code uses another for loop to iterate over the range from 0 to pnum. 
# Inside the loop, the input() function is used to get input from the user and convert it to an integer using the int() function. 
# The integer value is then added to the pnlist list using the append() method
# This integer value represents process number "i" our of a total of "pnum" blocks.
for i in range(pnum):
    psize = int(input(f"Enter process size for process number {i + 1}:\t"))
    pnlist.append(psize)

# The below code prints a header for the table that will be displayed later
print("Process No.          Process Size         Block No.")

# The below code uses a for loop to iterate over the range from 0 to pnum. 
# Inside the loop, there is another nested for loop that iterates over the range from 0 to bnum. 
# The purpose of this loop is to find the first block that can accommodate the current process. For example; (will P1 fit in B1,B2,B3,B4,B5) then (will P2 fit in B1,B2,B3,B4,B5)
# The if statement checks if the size of the current block is greater than or equal to the size of the current process,
# If these conditions are met, that process is assigned to the current block.
# If assigned a block, the process size is subtracted from the size of the block using the bnlist[j] = bnlist[j] - pnlist[i] line, updating the block size
# The process no., process size., and block no., are printed using the print() function.
# and that process is assumed to be "allocated", and "break" allows the for loop to stop checking any other blocks in that iteration.
for i in range(pnum):
    allocated = False 
    for j in range(bnum):
        if bnlist[j] >= pnlist[i]:
            bnlist[j] = bnlist[j] - pnlist[i]
            
            print(f"{i + 1}                     {pnlist[i]}                        {j + 1}")
            allocated = True
            break

# If a process was not assigned to a block, the process No and size is simply printed along with the message "Not Allocated".
    if not allocated:
        print(f"{i + 1}                     {pnlist[i]}                 Not Allocated")
