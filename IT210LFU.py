#IT 210 Q5 - Page Replacement Algorithm
#Created by: Divine Aluko - Adeolu Group 3
#148618


#LFU implentation
page_reference = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8]

physical_memory_size = 3
physical_memory = []

def page_in_memory(page):
    for i in range(len(physical_memory)):
        if physical_memory[i][0] == page:
            return i
    return -1

def get_lfu_page():
    lfu_page_index = 0
    for i in range(1, len(physical_memory)):
        if physical_memory[i][1] < physical_memory[lfu_page_index][1]:
            lfu_page_index = i
    return lfu_page_index

page_queue = []

for page in page_reference:
    for i in range(len(physical_memory)):
        if physical_memory[i][0] == page:
            physical_memory[i][1] += 1

    index = page_in_memory(page)

    if index == -1:
        page_queue.append(page)
    else:
        physical_memory[index][1] += 1

    if len(physical_memory) < physical_memory_size and index == -1:
        physical_memory.append([page, 1])

    elif index == -1:
        lfu_page_index = get_lfu_page()
        physical_memory[lfu_page_index] = [page, 1]

    num_pages = len(page_queue)
    print("Page References: ", page_reference)
    print("Physical Memory: ", physical_memory)
    print("Page Queue: ", page_queue)
    print("Number of Pages in Queue: ", num_pages)

print("LFU Page Replacement Algorithm Finished.")
