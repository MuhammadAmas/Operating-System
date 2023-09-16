from tabulate import tabulate

# Function to calculate the average waiting, turnaround, and completion time


def calculate_average_times(waiting_time, turnaround_time, completion_time):
    n = len(waiting_time)
    avg_waiting_time = sum(waiting_time) / n
    avg_turnaround_time = sum(turnaround_time) / n
    avg_completion_time = sum(completion_time) / n
    return avg_waiting_time, avg_turnaround_time, avg_completion_time

# Highest Response Ratio Next (HRRN) Scheduling


def hrrn_scheduling(num_processes, arrival_time, burst_time):
    completed = [0] * num_processes
    waiting_time = [0] * num_processes
    turnaround_time = [0] * num_processes
    completion_time = [0] * num_processes
    process = [f"p{i+1}" for i in range(num_processes)]

    sum_bt = sum(burst_time)
    avgwt = 0
    avgTT = 0
    t = arrival_time[0]

    data = []

    while t < sum_bt:
        hrr = -9999
        temp, loc = 0, 0

        for i in range(num_processes):
            if arrival_time[i] <= t and completed[i] != 1:
                temp = (
                    (burst_time[i] + (t - arrival_time[i])) / burst_time[i])

                if hrr < temp:
                    hrr = temp
                    loc = i

        t += burst_time[loc]
        completion_time[loc] = t
        waiting_time[loc] = (t - arrival_time[loc] - burst_time[loc])
        turnaround_time[loc] = t - arrival_time[loc]
        completed[loc] = 1
        avgwt += waiting_time[loc]

        data.append([process[loc], arrival_time[loc], burst_time[loc],
                    waiting_time[loc], turnaround_time[loc], completion_time[loc]])

    avg_waiting_time, avg_turnaround_time, avg_completion_time = calculate_average_times(
        waiting_time, turnaround_time, completion_time)
    data.append(["Average", "", "", "{:.6f}".format(avg_waiting_time), "{:.6f}".format(
        avg_turnaround_time), "{:.6f}".format(avg_completion_time)])

    headers = ["Name", "Arrival Time", "Burst Time",
               "Waiting Time", "Turnaround Time", "Completion Time"]

    print(tabulate(data, headers, tablefmt="grid"))

# Wrap the code in a function


def run_hrrn_scheduling():
    print("\n*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*")
    print("                    HRRN Scheduling Algorithm                        ")
    print("*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*\n")

    print(
        "Instruction: Please enter a number for the following: \n"
        + "\n\t*Number of Processes \n"
        + "\t*Burst time \n"
        + "\t*Arrival time \n"
    )
    num_processes, arrival_time, burst_time = input_process_details()

    hrrn_scheduling(num_processes, arrival_time, burst_time)

# Function to input process details


def input_process_details():
    num_processes = int(input("Enter the number of processes: "))
    arrival_time = []
    burst_time = []

    for i in range(num_processes):
        arrival = int(input(f"Enter arrival time for process p{i + 1}: "))
        burst = int(input(f"Enter burst time for process p{i + 1}: "))
        arrival_time.append(arrival)
        burst_time.append(burst)

    return num_processes, arrival_time, burst_time
