def banker_algorithm(n, m, available, max_need, allocation):
    # Initialize the needed and finish arrays
    need = [[max_need[i][j] - allocation[i][j] for j in range(m)] for i in range(n)]
    finish = [False] * n
    
    # Find a safe sequence if it exists
    sequence = []
    work = available.copy()
    while len(sequence) < n:
        found = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                finish[i] = True
                sequence.append(i)
                for j in range(m):
                    work[j] += allocation[i][j]
                found = True
        if not found:
            return None
    
    return sequence

if __name__ == "__main__":
    n = 5  # Number of processes
    m = 3  # Number of resource types
    available = [3, 3, 2]  # Available resources
    max_need = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]  # Maximum need of each process
    allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]  # Currently allocated resources for each process

    # Check if the system is in a safe state
    sequence = banker_algorithm(n, m, available, max_need, allocation)
    if sequence is not None:
        print("Safe sequence:", sequence)
    else:
        print("System is in an unsafe state")
