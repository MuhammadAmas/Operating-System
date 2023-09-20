from RR import run_rr_scheduling
from SRTF import run_srtf_scheduling
from SJF import run_sjf_scheduling
from HRRN import run_hrrn_scheduling


while True:
    user_choice = input(
        """Which scheduling algorithm do you want to use? 
        (RR) -> Round Robin 
        (SJF) -> Shortest Job First 
        (HRRN) -> Highest Response Ratio Next 
        (SRT) -> Shortest Remaining Time \n
        \rType the algorithm name short form: """).lower()
    print('\n\n')
    if user_choice == "rr":
        run_rr_scheduling()
    elif user_choice == "hrrn":
        run_hrrn_scheduling()
        break
    elif user_choice == "srt":
        run_srtf_scheduling()
        break
    elif user_choice == "sjf":
        run_sjf_scheduling()
        break
    else:
        print("Invalid choice. Please try again.")
