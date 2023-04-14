def allocation_of_blk(s_blk, no_blk):
    b_list = []
    for i in range(no_blk):
        b_list.append(str(s_blk+i))
    return "->".join(b_list)
i = 0
while i == 0:
    num_files = int(input("Enter the number of Files: "))
    print(" ")
    x = []
    for i in range(num_files):
        f_name = input("Enter file {} name: ".format(i+1))
        print(" ")
        f_size = int(input("Enter file{} f_size(in kb): ".format(i+1)))
        print(" ")
        s_blk = int(input("Enter Starting block of {}: ".format(i+1)))
        print(" ")
        blk_size = int(input("Enter blockf_size of {}(in bytes): ".format(i+1)))
        print(" ")
        no_blk = f_size*1024 // blk_size
        x.append([f_name, s_blk, no_blk])

    name = input("Enter the file name: ")
    print(" ")

    print("Fname\tStart\tNblocks\t\tBlocks")
    print("---------------------------------------------------")
    for i in x:
        if i[0] == name:
            print("{}\t{}\t{}\t\t{}".format(i[0], i[1], i[2], allocation_of_blk(i[1], i[2])))

    j = input("Do U want to continue (Y/N): ")

    if j == "Y" or j == "y":
        i = 0
    else:
        i = 1
