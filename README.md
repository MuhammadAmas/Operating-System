# Operating System

This repository contains operating system related material and various process scheduling algorithms implemented in Python.

## Scheduling Algorithms:
Scheduling algorithms are essential components of operating systems that manage the execution of multiple processes efficiently. They determine the order in which processes are executed, aiming to optimize resource utilization, response times, and overall system performance.


### 1. Round Robin (RR):
Round Robin is a preemptive scheduling algorithm that allocates each process a fixed time slice (quantum) to execute in a circular manner. It provides fairness and ensures that no process monopolizes the CPU for an extended period.

### 2. Shortest Remaining Time (SRT):
SRT is a preemptive scheduling algorithm that selects the process with the shortest remaining burst time whenever a new process arrives or the running process's burst time decreases. It ensures minimal waiting time and can lead to a more responsive system.


### 3. Shortest Job First (SJF):
SJF is a non-preemptive scheduling algorithm that selects the process with the shortest burst time to execute next. It minimizes waiting time and optimizes process turnaround time.


### 4. Highest Response Ratio Next (HRRN):
HRRN is a non-preemptive scheduling algorithm that selects the process with the highest response ratio (the ratio of waiting time to burst time) to execute next. It aims to provide fairness and minimize the average waiting time.


## Running the Scheduling Algorithms

#### Dependencies

Before running any of the scheduling algorithms, make sure you have the necessary dependencies installed. You can install them by running the install_dependencies.py file

```bash
python install_dependencies.py
```

To run a scheduling algorithm, navigate to the `Scheduling Algorithm` folder and execute the main.py file:

```python
python main.py
```
You will be prompted to choose a scheduling algorithm to run:

Highest Response Ratio Next (HRRN)
Shortest Job First (SJF)
Shortest Remaining Time (SRT)
Round Robin (RR)

Enter the corresponding abbrevation to choose an algorithm and follow the on-screen instructions to input any required parameters.

## Contributors
- **[Muhammad Amas](https://github.com/MuhammadAmas)**
- **[Zunain Ali Azam](https://github.com/ZunainAliAzam)**
- **[Ahmed Ali](https://github.com/Ahmad43A)**
- **[Ilhaam Ismail Soomro](https://github.com/ilhaamsoomro)**
- **[Shaheer Ali Zaidi](https://github.com/Syed-Shaheer-Ali-Zaidi)**
