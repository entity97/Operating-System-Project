####################################################################################### 
###                     Youssef Ibrahim 151912                                      ###
###                         IT 210 Project                                          ###
###     Question 1  CPU Scheduling Algorithms c) RR                                 ###
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
    arrival_time = int(input(f"Enter arrival time for process {process_id}: "))
     # Store each process ID and service time and arrival in the processes list such that the tuple is in the form(x,y,z)
    # where x would represent the automatically assigned process ID and y would represent the user-inputted service time and z the arrival time.

    processes.append((process_id, burst_time, arrival_time))

# Get time quantum from the user
time_quantum = int(input("Enter time quantum: "))

# Here we are initializing 2 lists and 2 varibles
# The waiting_times list will contain the waiting times for every process initialized to 0
# Remaining burst times will contain the remaining burst times for all process. Initialized with the burst times of each process from the input list
# completed processes will keep a count of process completed to notify completion.
# time is used to keep track of the current time.
waiting_times = [0] * num_processes
remaining_burst_times = [p[1] for p in processes]
completed_processes = 0
time = 0

# Calculate waiting times

while completed_processes < num_processes:
    # Iterate through each process
    for i in range(num_processes):
        # Check if the process has any burst time remaining and if it's arrival time is less than or equal to the current time
        if remaining_burst_times[i] > 0 and time >= processes[i][2]:
            # If the remaining burst time is greater than the time quantum, deduct the quantum from it and update the time accordingly
            if remaining_burst_times[i] > time_quantum:
                time += time_quantum
                remaining_burst_times[i] -= time_quantum
                # Otherwise, the remaining burst time is less than or equal to the time quantum
            else:
                # Update the time by adding the remaining burst time
                time += remaining_burst_times[i]
                # Calculate the waiting time for the process and update the waiting_times list
                waiting_times[i] = time - processes[i][1] - processes[i][2]
                # Set the remaining burst time for the process to 0
                remaining_burst_times[i] = 0
                # Increment the completed_processes counter
                completed_processes += 1

# Calculate the average waiting time and average turnaround time
# Calculate the average waiting time by dividing the total waiting time by the number of processes
# Calculate the total turnaround time by summing the waiting time and the burst time for each process
# Calculate the average turnaround time by dividing the total turnaround time by the number of processes
total_waiting_time = sum(waiting_times)
average_waiting_time = total_waiting_time / num_processes
total_turnaround_time = sum(waiting_times[i] + processes[i][1] for i in range(num_processes))
average_turnaround_time = total_turnaround_time / num_processes

# Print the results
print(f"Average waiting time: {average_waiting_time}")
print(f"Average turnaround time: {average_turnaround_time}")