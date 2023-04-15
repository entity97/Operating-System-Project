####################################################################################### 
###                     Youssef Ibrahim 151912                                      ###
###                         IT 210 Project                                          ###
###     Question 1  CPU Scheduling Algorithms a) FCFS                               ###
#######################################################################################

# Here we are asking the user for the number of processes that they are to input
num_processes = int(input("Enter the number of processes: "))

# Here we are initializing a list, that will contain the process ID and service time for each process for a total of "num_processes" processes
processes = []

# Here we are using a for loop from 0 to "num_processes" to get the Service time for each process from the user, the ID is assigned automatically.
for i in range(num_processes):
    process_id = i + 1
    # Prompt user to input the service time for each process
    service_time = int(input(f"Enter service time for process {process_id}: "))
    # Store each process ID and service time as a tuple in the processes list such that the tuple is in the form(x,y)
    # where x would represent the automatically assigned process ID and y would represent the user-inputted service time.
    processes.append((process_id, service_time))

# Here we are initializing 2 lists
# The waiting_times list will contain the waiting times for every process
# The total_times will contain the total time for every process,
# it is initialized as the service time of the first process(shown by processes[0][1]) rather than traditionally with 0.
waiting_times = [0]
total_times = [processes[0][1]]

# Here we are using a for loop to iterate through each process in the order it was inputted. The order of process arrival is assumed to be the order of input.
# We use this for loop to calculate waiting time, total time for each processes.
# We calculate waiting time for the current process as the total time of the previous process
# We calculate total time for the current process as the sum of its service time and waiting time
for i in range(1, num_processes):
    waiting_times.append(total_times[i-1])
    total_times.append(waiting_times[i] + processes[i][1])

# Here we calculate total waiting time and total turnaround time
# Sum up all the elements in the waiting_times list to get the total waiting time
# Sum up all the elements in the total_times list to get the total turnaround time
total_waiting_time = sum(waiting_times)
total_turnaround_time = sum(total_times)

# Calculate average waiting time and print it to the user
# Divide the total waiting time by the number of processes to get the average waiting time
average_waiting_time = total_waiting_time / num_processes

# Print the average waiting time to the user
print(f"Average waiting time: {average_waiting_time}")

# Calculate average turnaround time and print it to the user
# Divide the total turnaround time by the number of processes to get the average turnaround time
average_turnaround_time = total_turnaround_time / num_processes

# Print the average turnaround time to the user
print(f"Average turnaround time: {average_turnaround_time}")
