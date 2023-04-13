#IT 210 Q5 - Page Replacement Algorithm
#Created by: Divine Aluko - Adeolu Group 3
#148618

print("FIFO page replacement algorithm")


size = int(input("Enter cache size: "))


num_pages = int(input("Enter number of pages: "))


counter = 0
stack = []


for i in range(num_pages):
    page = input("Enter page value: ")

    
    if page in stack:
        stack.remove(page)
    else:
        if len(stack) == size:
            stack.pop(0)
        counter += 1
    
    stack.append(page)

    
    print(f"Page {page} inserted into cache: {stack}")
    

print("FIFO page replacement algorithm completed")



