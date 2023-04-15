####################################################################################### 
###                     Youssef Ibrahim 151912                                      ###
###                         IT 210 Project                                          ###
###     Question 1  CPU Scheduling Algorithms c) PS                                 ###
#######################################################################################

# Here we are asking the user for the number of processes that they are to input
num_processes = int(input("Enter the number of processes: "))

# Here we are initializing a list, that will contain the process ID and service time for each process for a total of "num_processes" processes
processes = []
# Here we are using a for loop from 0 to "num_processes" to get the Service time for each process from the user, the ID is assigned automatically.
for i in range(num_processes):
    process_id = i + 1
   # Prompt user to input the service time for each process

    burst_time = int(input(f"Enter burst time for process {process_id}: "))
    priority = int(input(f"Enter priority (1-high 10-low) for process {process_id}: "))
    # Store each process ID and service time and priority in the processes list such that the tuple is in the form(x,y,z)
    # where x would represent the automatically assigned process ID and y would represent the user-inputted service time and z the priority.

    processes.append((process_id, burst_time, priority))

#Here we are using the .sort() method with argument lambda x[2] to sort the processes in order of priority
processes.sort(key=lambda x: x[2])


# Here we are initializing 2 lists
# The waiting_times list will contain the waiting times for every process
# The turnaround_times will contain the total time for every process,
# it is initialized as the service time of the first process(shown by processes[0][1]) rather than traditionally with 0.
waiting_times = [0] * num_processes
turnaround_times = [0] * num_processes
turnaround_times[0] = processes[0][1]
# Here we are using a for loop to iterate through each process in the order it was inputted. The order of process arrival is assumed to be the order of input.
# We use this for loop to calculate waiting time, turnaround time for each processes.
# We calculate waiting time for the current process as the total time of the previous process
# We calculate turnaround time for the current process as the sum of its service time and waiting time
for i in range(1, num_processes):
    waiting_times[i] = waiting_times[i - 1] + processes[i - 1][1]
    turnaround_times[i] = waiting_times[i] + processes[i][1]

# Here we calculate total waiting time and total turnaround time
# Sum up all the elements in the waiting_times list to get the total waiting time
# Sum up all the elements in the total_times list to get the total turnaround time
total_waiting_time = sum(waiting_times)
total_turnaround_time = sum(turnaround_times)

# Calculate average waiting time and print it to the user
# Divide the total waiting time by the number of processes to get the average waiting time
average_waiting_time = total_waiting_time / num_processes

# Calculate average turnaround time and print it to the user
# Divide the total turnaround time by the number of processes to get the average turnaround time
average_turnaround_time = total_turnaround_time / num_processes

# Print the results
print(f"Average waiting time: {average_waiting_time}")
print(f"Average turnaround time: {average_turnaround_time}")
