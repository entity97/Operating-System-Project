class File:
    def __init__(self, fname,fsize, start, end, size, blocks):
        self.fname = fname
        self.fsize = fsize
        self.start = start
        self.size = size
        self.blocks = blocks
        self.end = end

def link_allocation(start, end, blocks):
    b_list = []
    b_list.append(str(start))
    for i in range(len(blocks)):
        b_list.append(str(blocks[i]))
    b_list.append(str(end))    
    return "->".join(b_list)


n = int(input("Enter no. of files: "))
print(" ")
files = []
for i in range(n):
    fname = input("Enter file {} name: ".format(i+1))
    fsize = int(input("Enter file {} size(in kb): ".format(i+1)))
    size = int(input("Enter the block size of file {}: ".format(i+1)))
    print(" ")
    no_blk = fsize*1024 // size   
    start = int(input("Enter starting block of file {}: ".format(i+1)))
    end = int(input("Enter ending block of file {}: ".format(i+1)))
    print(" ")
    print("Enter blocks for file {}: ".format(i+1))
    blocks = []
    for j in range(no_blk):    
        block = int(input("Enter the {} block: ".format(j+1)))
        blocks.append(block)
    print(" ")
    files.append([fname,fsize,size, start,blocks, end, no_blk])

i = 0
while i == 0:
    name = input("Enter the file name: ")
    print(" ")

    print("Fname\tFsize\tBsize\tNblocks\tBlocks")
    print("---------------------------------------------------")

    for file in files:
        if file[0] == name:
            print("{}\t{}\t{}\t{}\t{}".format(file[0], file[1], file[2], file[6], link_allocation(file[3], file[5], file[4])))
    print(" ")
    j = input("Do U want to continue (Y/N): ")

    if j == "Y" or j == "y":
        i = 0
    else:
        i = 1