####################################################################################### 
###                     Youssef Ibrahim 151912                                      ###
###                         IT 210 Project                                          ###
###     Question 4  Memory Allocation Methods-Fixed Partition b) Best Fit           ###
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
# The purpose of this loop is to find the best block that can accommodate the current process.
# The if statement checks if the size of the current block is greater than or equal to the size of the current process,
# and if the difference between the block size and the process size is less than the current minimum difference. 
# If these conditions are met, the current block is considered the best block so far.
# After the nested for loop completes, the code checks whether a best block was found. 
# If a best block was found, the process size is subtracted from the size of the best block using the -= operator,
# and the process no., process size., and block no., are printed using the print() function.
# If a best block was not found, the process No and size is simply printed along with the message "Not Allocated".

for i in range(pnum):
    min_diff = float('inf') 
    # min_diff is initialized to positive infinity using the float() function with the argument 'inf'. 
    # The purpose of this variable is to keep track of the minimum difference between a block size and a 
    # process size that has been found so far. This value is initialized to infinity so that the first difference 
    # that is found will always be smaller than the current value of min_diff.

    best_block = -1
    #best_block is initialized to -1. This variable is used to keep track of the index of the best block that has been
    # found so far. The -1 value is used as a sentinel value that indicates that no best block has been found yet. 
    # If no block is found that can accommodate a given process, the value of best_block will remain -1 and the process 
    # will not be allocated to any block.

    for j in range(bnum):
        if bnlist[j] >= pnlist[i] and bnlist[j] - pnlist[i] < min_diff:
            min_diff = bnlist[j] - pnlist[i]
            best_block = j

    if best_block != -1:
        bnlist[best_block] -= pnlist[i]
        print(f"{i + 1}                     {pnlist[i]}                        {best_block + 1}")
    else:
        print(f"{i + 1}                     {pnlist[i]}                 Not Allocated")
