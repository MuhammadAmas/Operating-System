def run_srtf_scheduling():
    print("\n*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*")
    print("                    SRTF Scheduling Algorithm                        ")
    print("*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*~~~~~*\n")

    print(
        "Instruction: Please enter a number for the following: \n"
        + "\n\t*Number of Processes (with min. of 5 and max. of 10) \n"
        + "\t*Burst time (with min. of 5 and max. of 15 each) \n"
        + "\t*Arrival time (with min. of 1 and max. of 12 each) \n"
    )

    pid = []
    while True:
        try:
            n = int(input("Number of Processes: "))
            if n >= 5 and n <= 10:
                i = 0
                j = 1
                while i != n:
                    if n + 1 != j:
                        pid.append("P" + str(j))
                        j += 1
                    i += 1
                break
            else:
                print("\n'Invalid input. Please enter number 5 to 10 only.'\n")
        except ValueError:
            print("\n'Invalid input. Please enter an integer.'\n")

    burst_remaining = [0] * (len(pid) + 1)
    burst_time = [0] * (len(pid) + 1)
    arrival_time = [0] * (len(pid) + 1)
    first_occur = [0] * (len(pid) + 1)
    completion_time = [0] * (len(pid) + 1)
    turnaround_time = [0] * (len(pid) + 1)
    waiting_time = [0] * (len(pid) + 1)
    response_time = [0] * (len(pid) + 1)

    h = 1
    while h < n + 1:
        burst_time[h] = input('\nBurst Time of "P%d": ' % h)
        if burst_time[h].isnumeric():
            burst_time[h] = int(burst_time[h])
            if burst_time[h] >= 5 and burst_time[h] <= 15:
                burst_remaining[h] = burst_time[h]
                boolean = True
                while boolean == True:
                    arrival_time[h] = input('Arrival Time of "P%d": ' % h)
                    if arrival_time[h].isnumeric():
                        arrival_time[h] = int(arrival_time[h])
                        if arrival_time[h] >= 1 and arrival_time[h] <= 12:
                            pass
                            boolean = False
                        else:
                            arrival_time[h] = 0
                            print(
                                "'Invalid input. Please enter from number 1 to 12 only.'")
                    else:
                        print("'Invalid input. Please enter an integer.'")
            else:
                burst_time[h] = 0
                print("'Invalid input. Please enter from number 5 to 15 only.'")
                h = h - 1
        else:
            print("'Invalid input. Please enter an integer.'")
            h = h - 1
        h = h + 1

    burst_time.pop(0)
    arrival_time.pop(0)
    burst_remaining.pop(0)

    is_completed = [0] * (len(pid) + 1)
    avg_turn_around_time = None
    avg_waiting_time = None
    total_turnaround_time = 0
    total_waiting_time = 0

    current_time = 0
    completed = 0
    gantt_pid = []

    while completed != n:
        idx = -1

        mn = 1000000
        for i in range(0, n):
            if arrival_time[i] <= current_time and is_completed[i] == 0:
                if burst_remaining[i] < mn:
                    mn = burst_remaining[i]
                    idx = i

                if burst_remaining[i] == mn:
                    if arrival_time[i] < arrival_time[idx]:
                        mn = burst_remaining[i]
                        idx = i

        if idx != -1:
            if burst_remaining[idx] == burst_time[idx]:
                first_occur[idx] = current_time

            burst_remaining[idx] -= 1
            current_time += 1

            if burst_remaining[idx] == 0:
                completion_time[idx] = current_time
                turnaround_time[idx] = completion_time[idx] - arrival_time[idx]
                waiting_time[idx] = turnaround_time[idx] - burst_time[idx]
                response_time[idx] = first_occur[idx] - arrival_time[idx]
                total_turnaround_time += turnaround_time[idx]
                total_waiting_time += waiting_time[idx]

                is_completed[idx] = 1
                completed += 1

        else:
            current_time += 1

        if idx >= 0:
            gantt_pid.append("P" + str(idx + 1))
        else:
            gantt_pid.append("P" + str(idx + 2))
            gantt_pid.pop(0)

    avg_waiting_time = round(float(total_waiting_time) / n, 2)
    avg_turn_around_time = round(float(total_turnaround_time) / n, 2)

    print("\nLEGEND:")
    print("    __________________________ ____________________________ ")
    print("   |                          |                            |")
    print("   | AT =  'Arrival Time'     |   TAT = 'Turnaround Time'  |")
    print("   | BT =  'Burst Time'       |   WT =  'Waiting Time'     |")
    print("   | CT =  'Completion Time'  |   RT =  'Response Time'    |")
    print("   |__________________________|____________________________|")

    tbl_header = [" Process", "AT", "BT", "CT", "TAT", "WT", "RT"]
    ln = "   —————————————————————————————————————————————————————————————"
    print("\n\nTable:")
    print(ln)
    print(
        "  |"
        + tbl_header[0].center(12)
        + " |"
        + tbl_header[1].center(7)
        + "|"
        + tbl_header[2].center(7)
        + "|"
        + tbl_header[3].center(7)
        + "|"
        + tbl_header[4].center(7)
        + "|"
        + tbl_header[5].center(7)
        + "|"
        + tbl_header[6].center(7)
        + "|"
    )
    print(ln)
    for i in range(0, n):
        print(
            "  |"
            + str(pid[i]).center(12)
            + " |"
            + str(arrival_time[i]).center(7)
            + "|"
            + str(burst_time[i]).center(7)
            + "|"
            + str(completion_time[i]).center(7)
            + "|"
            + str(turnaround_time[i]).center(7)
            + "|"
            + str(waiting_time[i]).center(7)
            + "|"
            + str(response_time[i]).center(7)
            + "|"
        )
    print(ln)

    if 0 not in arrival_time:
        gantt_pid.insert(0, "")

    gantt_pid = [
        v for i, v in enumerate(gantt_pid) if i == 0 or v != gantt_pid[i - 1]
    ]

    gantt_bt = sorted(set(first_occur + completion_time))
    gantt_length = []

    for i in range(len(gantt_bt) - 1):
        sub = gantt_bt[i + 1] - gantt_bt[i]
        gantt_length.append(sub)

    gantt_length.append(0)
    print("\nGantt Chart:\n")

    while boolean != True:
        for i in range(len(gantt_pid)):
            temp = str(gantt_pid[i])
            print(" " + temp.center(int(gantt_length[i] + 1)), end="")
        print()
        for i in range(len(gantt_pid)):
            print("|" + ("-" * (int(gantt_length[i] + 1))), end="")
        print("|")
        boolean = True

    for i in range(0, len(gantt_bt)):
        if gantt_bt[i] <= 9 and gantt_bt[i] < 99:
            print(str(gantt_bt[i]) + (str(" ") *
                  int(gantt_length[i] - 1)), end="  ")
        elif gantt_bt[i] > 9 and gantt_bt[i] <= 99:
            print(str(gantt_bt[i]) + (str(" ") *
                  int(gantt_length[i] - 1)), end=" ")
        elif gantt_bt[i] > 9 and gantt_bt[i] > 99:
            print(str(gantt_bt[i]) + (str(" ") *
                  int(gantt_length[i] - 1)), end="")

    print(
        "\n\nAverage Waiting Time (AWT): ",
        avg_waiting_time,
        "ms",
        "\nAverage Turnaround Time (ATT): ",
        avg_turn_around_time,
        "ms",
    )
