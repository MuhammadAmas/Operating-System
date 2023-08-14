class ProcessControlBlock:
    def __init__(self, pid, arrival_time, execution_time, quantum_size, resource, no_of_instructions):
        self.pid = pid
        self.arrival_time = arrival_time
        self.execution_time = execution_time
        self.remaining_execution_time = execution_time
        self.quantum_size = quantum_size
        self.resource = resource
        self.no_of_instructions = no_of_instructions
        self.turn_around_time = 0
        self.utilization_time = 0
        self.scheduling_algo = "Round Robin"
        self.finish_time = None

def round_robin_scheduling(processes, time_quantum):
    current_time = 0
    completed_processes = []
    ready_queue = []
    running_process = None

    while processes or ready_queue or running_process:
        while processes and processes[0].arrival_time <= current_time:
            process = processes.pop(0)
            ready_queue.append(process)

        if running_process is None and ready_queue:
            running_process = ready_queue.pop(0)
            print(f"Process P{running_process.pid} added to ready queue at Time {current_time}")
            print(f"Process P{running_process.pid} loaded into running queue at Time {current_time}")
            print(f"Time {current_time}: Process P{running_process.pid} starts execution")

        if running_process:
            execution_time = min(time_quantum, running_process.remaining_execution_time)
            running_process.remaining_execution_time -= execution_time
            current_time += execution_time

            if running_process.remaining_execution_time == 0:
                running_process.finish_time = current_time
                running_process.turn_around_time = running_process.finish_time - running_process.arrival_time
                running_process.utilization_time = running_process.execution_time - running_process.remaining_execution_time
                completed_processes.append(running_process)
                print(f"Time {current_time}: Process P{running_process.pid} finishes execution")
                running_process = None
            elif ready_queue:
                ready_queue.append(running_process)
                print(f"Time {current_time}: Process P{running_process.pid} is preempted and added back to the queue")
                running_process = ready_queue.pop(0)
                print(f"Time {current_time}: Process P{running_process.pid} resumes execution")
                
            else:
                print(f"Time {current_time}: Process P{running_process.pid} continues execution")

    return completed_processes

def main():
    num_processes = int(input("How many processes do you want to create (minimum 3, maximum 5): "))
    if num_processes < 3 or num_processes > 5:
        print("Invalid number of processes. Please enter a number between 3 and 5.")
        return

    time_quantum = int(input("Enter time quantum for all processes: "))

    processes = []
    for pid in range(1, num_processes + 1):
        arrival_time = 0 if pid == 1 else int(input(f"Enter arrival time for process P{pid}: "))
        execution_time = int(input(f"Enter execution time for process P{pid} (<= 10): "))
        if execution_time > 10:
            print("Execution time must be <= 10. Please re-enter the execution time.")
            return
        resource = str(input(f"Enter resource desired for process P{pid} : "))
        no_of_instructions = str(input(f"Enter number of instructions in process P{pid} : "))
        

        processes.append(ProcessControlBlock(pid, arrival_time, execution_time, time_quantum, resource, no_of_instructions))

    completed_processes = round_robin_scheduling(processes, time_quantum)

    print("\nProcess Control Information for Completed Processes:")
    for process in completed_processes:
        print(f"PCB for Process P{process.pid}:")
        print(f"  Arrival Time: {process.arrival_time}")
        print(f"  Execution Time: {process.execution_time}")
        print(f"  Quantum Size: {process.quantum_size}")
        print(f"  Turn Around Time: {process.turn_around_time}")
        print(f"  Utilization Time: {process.utilization_time}")
        print(f"  Scheduling Algorithm: {process.scheduling_algo}")
        print(f"  Resource : {process.resource}")
        print(f"  No of instructions : {process.no_of_instructions}")
        print(f"  Finish Time: {process.finish_time}")
        print()

if __name__ == "__main__":
    main()
