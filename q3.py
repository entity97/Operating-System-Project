"""Deadlock Detection Algorithm
    by Mohammad Sadav Imtiaz Alam, Student ID: 149812
    
    This script allows the user to detect deadlocks in a given number of processes.
    
    The print_resources function uses numpy array indexing instead of nested loops to optimize 
    the numerical operations and efficiently using the memory access and caching. 
    
    The can_finish function takes the allocation, max, and available resource matrices as arguments
    which then checks whether the processes can finish execution or not.
    
    The detect_deadlock function is the script's key function, which implements the deadlock
    detection algorithm. Uses numpy to represent the allocation, max, and available resource matrices
    and the finished array to keep track of which processes have finished. The function goes over
    the processes repeatedly and checks whether they can end; if they can, they are marked finished
    and if no process can finish, the function stops and reports a deadlock detection. If all
    processes finish before a deadlock is detected, the function prints no deadlock detected. 
    
    The main block takes the premade allocation, max, and available resource matrices from the
    example as numpy arrays and calls the print_resources and detect_deadlock functions with these
    inputs. And as per the algorithm, the output is then generated.
"""


import numpy as np

def print_resources(allocation, max, available):
"""prints the resource allocation matrix and available resources

    Args:
        allocation (numpy.ndarray): The allocation matrix of shape (n,m) where n is the number of 
            processees and m is the number of resources. 
        max (numpy.ndarray): The maximum demand matrix of shape (n,m) where n is the number of
            processes and m is the number or resources.
        available (numpy.ndarray): The available resources vector of shape (m) where m is the
            number of resources.
     
     Returns:
        None.
"""

    print("Resource allocation:")
    for i in range(allocation.shape[0]):
        print("P{} ".format(i), end='')
        for j in range(allocation.shape[1]):
            print("{} ".format(allocation[i][j]), end='')
        print("| ", end='')
        for j in range(max.shape[1]):
            print("{} ".format(max[i][j]), end='')
        print("")
    print("Available: ", end='')
    for i in range(available.shape[0]):
        print("{} ".format(available[i]), end='')
    print("")

def can_finish(process, allocation, max, available):
"""checks if a process can finish execution by comparing its maximum resource needs to its 
    current allocation and available resources.

    Args:
        processes (int): Index of the process being checked. 
        allocation (numpy.ndarray): Array representing the current allocation of resources to
            processes.
        max (numpy.ndarray): Array representing the maximum resources needs of processes. 
        available (numpy.ndarray): Array representing the currently available resources.
     
     Returns:
        bool: True if the process can finish execution, i.e. its maximum process needs can be
        satisfied with its current allocation and available resources, without leading to 
        deadlock; False otherwise.
"""
    for i in range(allocation.shape[1]):
        if max[process][i] - allocation[process][i] > available[i]:
            return False
    return True

#Define a function to detect whether deadlock is present or not
def detect_deadlock(allocation, max, available):
"""detects deadlock for the given example.

    Args:
        allocation (numpy.ndarray): Array representing the current allocation of resources to
            processes.
        max (numpy.ndarray): Array representing the maximum resources required by each process. 
        available (numpy.ndarray): Array representing the currently available resources.
     
     Returns:
        bool: True if deadlock is detected; False otherwise.
"""  
    num_processes = allocation.shape[0]
    finished = np.zeros(num_processes, dtype=bool)
    found = False

    #Loop untill all processes are finished or deadlock is detected
    while np.sum(finished) < num_processes:
        finished_this_iteration = False

        #check each process to see if it can finish execution
        for i in range(num_processes):
            if not finished[i] and can_finish(i, allocation, max, available):
                finished_this_iteration = True
                finished[i] = True

                #release resources held by the process and add them to available resources
                for j in range(allocation.shape[1]):
                    available[j] += allocation[i][j]
                    allocation[i][j] = 0

        #if no process can finish execution, deadlock is present
        if not finished_this_iteration:
            found = True
            print("System is in deadlock and deadlock processes are: ", end='')
            for i in range(num_processes):
                if not finished[i]:
                    print("P{} ".format(i), end='')
            print("")
            break
        #if all processes finish execution, deadlock is not present
        else:
            found = False
            print("No deadlock detected")
    return found

if __name__ == '__main__':
    num_processes = 3
    num_resources = 3
    max = np.array([[3, 6, 8], [4, 3, 3], [3, 4, 4]])
    allocation = np.array([[3, 3, 3], [2, 0, 3], [1, 2, 4]])
    available = np.array([1, 2, 0])

    print_resources(allocation, max, available)
    detect_deadlock(allocation, max, available)
