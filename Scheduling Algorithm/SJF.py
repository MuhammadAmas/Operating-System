from prettytable import PrettyTable

def sjf_scheduling(process_data):
    start_time = []
    exit_time = []
    s_time = 0
    process_data.sort(key=lambda x: x[1])
    gantt_chart = []  # Initialize Gantt chart

    for i in range(len(process_data)):
        ready_queue = []
        temp = []
        normal_queue = []

        for j in range(len(process_data)):
            if (process_data[j][1] <= s_time) and (process_data[j][3] == 0):
                temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                ready_queue.append(temp)
                temp = []
            elif process_data[j][3] == 0:
                temp.extend([process_data[j][0], process_data[j][1], process_data[j][2]])
                normal_queue.append(temp)
                temp = []

        if len(ready_queue) != 0:
            ready_queue.sort(key=lambda x: x[2])
            start_time.append(s_time)
            s_time += ready_queue[0][2]
            e_time = s_time
            exit_time.append(e_time)
            for k in range(len(process_data)):
                if process_data[k][0] == ready_queue[0][0]:
                    break
            process_data[k][3] = 1
            process_data[k].append(e_time)
            gantt_chart.append([ready_queue[0][0], start_time[-1], e_time])

        elif len(ready_queue) == 0:
            if s_time < normal_queue[0][1]:
                s_time = normal_queue[0][1]
            start_time.append(s_time)
            s_time += normal_queue[0][2]
            e_time = s_time
            exit_time.append(e_time)
            for k in range(len(process_data)):
                if process_data[k][0] == normal_queue[0][0]:
                    break
            process_data[k][3] = 1
            process_data[k].append(e_time)
            gantt_chart.append([normal_queue[0][0], start_time[-1], e_time])

    avg_turnaround_time = calculate_turnaround_time(process_data)
    avg_waiting_time = calculate_waiting_time(process_data)
    for i in range(len(process_data)):
        process_data[i][0] = "P"+str(process_data[i][0])
    return process_data, avg_turnaround_time, avg_waiting_time, gantt_chart

def display_gantt_chart(gantt_chart):
    for row in gantt_chart:
        print(f" P{row[0]}" + " " * (row[2] - row[1]), end="")
    print()
    for row in gantt_chart:
        print("|" + "-" * (row[2] - row[1] + 1), end="")
    print("|")
    for row in gantt_chart:
        print(f"{row[1]}", end="")
        print(" " * (row[2] - row[1] - len(str(row[1]))), end="  ")
    print(row[2], end="")
    print()

def calculate_turnaround_time(process_data):
    total_turnaround_time = 0
    for i in range(len(process_data)):
        turnaround_time = process_data[i][4] - process_data[i][1]
        total_turnaround_time += turnaround_time
        process_data[i].append(turnaround_time)
    return total_turnaround_time / len(process_data)

def calculate_waiting_time(process_data):
    total_waiting_time = 0
    for i in range(len(process_data)):
        waiting_time = process_data[i][5] - process_data[i][2]
        total_waiting_time += waiting_time
        process_data[i].append(waiting_time)
    return total_waiting_time / len(process_data)

def run_sjf_scheduling():
    while True:
        try:
            no_of_processes = int(input("Enter number of processes (3 to 10): "))
            if 3 <= no_of_processes <= 10:
                break
            else:
                print("Invalid input. Please enter a number between 3 and 10.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    process_data = []

    for i in range(no_of_processes):
        arrival_time = int(input(f"Enter Arrival Time for Process {i + 1}: "))
        burst_time = int(input(f"Enter Burst Time for Process {i + 1}: "))
        process_data.append([i + 1, arrival_time, burst_time, 0])

    result, avg_turnaround_time, avg_waiting_time, gantt_chart = sjf_scheduling(process_data)

    result_table = PrettyTable()
    result_table.field_names = ["Process_ID", "Arrival_Time", "Burst_Time","Completed", "Completion_Time", "Turnaround_Time", "Waiting_Time"]

    for process in result:
        result_table.add_row(process)
    print(result_table)

    print(f'Average Turnaround Time: {avg_turnaround_time}')
    print(f'Average Waiting Time: {avg_waiting_time}')

    print("\nGantt Chart:")
    display_gantt_chart(gantt_chart)
