from tabulate import tabulate


class ProcessControlBlock:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0
        self.completion_time = 0
        self.response_ratio = 0


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def is_empty(self):
        return len(self.queue) == 0


def calculate_average_times(processes):
    n = len(processes)
    avg_waiting_time = sum(p.waiting_time for p in processes) / n
    avg_turnaround_time = sum(p.turnaround_time for p in processes) / n
    avg_completion_time = sum(p.completion_time for p in processes) / n
    return avg_waiting_time, avg_turnaround_time, avg_completion_time


def display_pcb(processes):
    print("\nProcess Control Block:")
    headers = ["Process ID", "Arrival Time", "Burst Time", "Waiting Time",
               "Turnaround Time", "Completion Time", "Response Ratio"]
    data = []

    for p in processes:
        data.append([p.process_id, p.arrival_time, p.burst_time, p.waiting_time,
                     p.turnaround_time, p.completion_time, p.response_ratio])

    print(tabulate(data, headers, tablefmt="grid"))


def hrrn_scheduling(num_processes, arrival_time, burst_time):
    process_queue = Queue()
    processes = []

    for i in range(num_processes):
        pcb = ProcessControlBlock(f'P{i + 1}', arrival_time[i], burst_time[i])
        processes.append(pcb)
        process_queue.enqueue(pcb)

    t = 0
    data = []

    while not process_queue.is_empty():
        eligible_processes = [
            p for p in process_queue.queue if p.arrival_time <= t]
        if not eligible_processes:
            t += 1
            continue

        hrr = -9999
        selected_process = None

        for p in eligible_processes:
            p.response_ratio = (
                p.burst_time + (t - p.arrival_time)) / p.burst_time
            if p.response_ratio > hrr:
                hrr = p.response_ratio
                selected_process = p

        t += selected_process.burst_time
        selected_process.completion_time = t
        selected_process.waiting_time = t - \
            selected_process.arrival_time - selected_process.burst_time
        selected_process.turnaround_time = t - selected_process.arrival_time
        process_queue.queue.remove(selected_process)

        data.append([selected_process.process_id, selected_process.arrival_time,
                     selected_process.burst_time, selected_process.waiting_time,
                     selected_process.turnaround_time, selected_process.completion_time])

        display_pcb(processes)

        # Display the queue
        queue_ids = [p.process_id for p in process_queue.queue]
        print(f"Processes in Queue at time {t}: {queue_ids}")

    avg_waiting_time, avg_turnaround_time, avg_completion_time = calculate_average_times(
        processes)
    data.append(["Average", "", "", "{:.6f}".format(avg_waiting_time),
                 "{:.6f}".format(avg_turnaround_time), "{:.6f}".format(avg_completion_time)])

    headers = ["Process ID", "Arrival Time", "Burst Time",
               "Waiting Time", "Turnaround Time", "Completion Time"]

    print('\n\n', 'Final Result')
    print(tabulate(data, headers, tablefmt="grid"))


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


def input_process_details():
    num_processes = int(input("Enter the number of processes: "))
    arrival_time = []
    burst_time = []

    for i in range(num_processes):
        arrival = int(input(f"Enter arrival time for process {i + 1}: "))
        burst = int(input(f"Enter burst time for process {i + 1}: "))
        arrival_time.append(arrival)
        burst_time.append(burst)

    print('\n\n')
    return num_processes, arrival_time, burst_time

def main():
    run_hrrn_scheduling()

if __name__ == "__main__":
    main()