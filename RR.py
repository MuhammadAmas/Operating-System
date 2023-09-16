import random
from prettytable import PrettyTable


def trigger_function():
    if random.random() < 0.3:
        return True
    else:
        return False


class Process:
    counter = 0

    def __init__(self, processid, executiontime):
        self.processid = processid
        self.resume = 1
        self.executiontime = executiontime
        self.executed = 0
        self.isexecuted = False
        self.state = 'R'
        self.resource = False


class PCB:
    def __init__(self, NProcess, Quantumsize, Executiontime):
        self.nprocess = NProcess
        self.quantumsize = Quantumsize
        self.processlist = [None] * self.nprocess
        self.IR = 0
        self.PC = 0

        for i in range(self.nprocess):
            tempprocess = Process(i + 1, Executiontime[i])
            self.processlist[i] = tempprocess
        self.roundrobin()

    def roundrobin(self):
        while not self.isallexecute():
            if not self.processlist[self.PC].isexecuted:
                currentprocess = self.processlist[self.PC]
                if trigger_function():
                    currentprocess.resource = True

                if currentprocess.resource:
                    currentprocess.state = 'B'
                    currentprocess.executed += 1
                    self.IR = currentprocess.resume
                    self.PC = self.assignPC(self.PC)
                    currentprocess.resume += 1
                    self.printPCB(currentprocess, self.quantumsize)
                    currentprocess.state = 'R'
                    currentprocess.resource = False

                else:
                    rem = currentprocess.executiontime - currentprocess.executed
                    if rem <= self.quantumsize:
                        self.IR = currentprocess.resume + rem - 1
                        currentprocess.executed = currentprocess.executiontime
                        currentprocess.resume = -1
                        self.PC = self.assignPC(self.PC)
                        self.printPCB(currentprocess, self.quantumsize)
                        currentprocess.isexecuted = True

                    else:
                        self.IR = currentprocess.resume + self.quantumsize - 1
                        self.PC = self.assignPC(self.PC)
                        currentprocess.resume += self.quantumsize
                        currentprocess.executed += self.quantumsize
                        self.printPCB(currentprocess, self.quantumsize)

    def assignPC(self, processid):
        i = (processid + 1) % self.nprocess
        while True:
            if not self.processlist[i].isexecuted:
                return i

            else:
                i = (i + 1) % self.nprocess
                if i == processid and not self.processlist[i].isexecuted:
                    return i
        return -1

    def isallexecute(self):
        for i in range(self.nprocess):
            if not self.processlist[i].isexecuted:
                return False
        return True

    def printPCB(self, myprocess, QT):
        if not myprocess.isexecuted:
            table = PrettyTable()
            print("PCB of Process", myprocess.processid, ": ")
            table.field_names = ["Field", "Value"]
            table.add_row(["Scheduling Algorithm", "Round Robin"])
            table.add_row(["Quantum size", QT])
            table.add_row(["Execution time", myprocess.executiontime])
            if (self.processlist[self.PC].resume <= 0):
                table.add_row(["Value of PC", f"all instructions executed"])
            else:
                table.add_row(
                    ["Value of PC", f"process {self.PC + 1} [ instruction {self.processlist[self.PC].resume} ]"])

            if myprocess.resource:
                table.add_row(
                    ["Resource required", f"process {myprocess.processid} [ instruction {self.IR} ]"])
            else:
                table.add_row(
                    ["Value of IR", f"process {myprocess.processid} [ instruction {self.IR} ]"])
                executed_str = ", ".join([str(i + 1)
                                         for i in range(myprocess.executed)])
                remaining_str = ", ".join(
                    [str(i + 1) for i in range(myprocess.executed, myprocess.executiontime)])
                table.add_row(["Executed instructions",
                              f"[ instruction {executed_str} ]"])
                table.add_row(
                    ["Remaining instructions", f"[ {remaining_str} ]"])

            if myprocess.resume >= 0:
                table.add_row(
                    ["Will resume from", f"process {myprocess.processid} [ instruction {myprocess.resume} ]"])
            else:
                table.add_row(
                    ["Will resume from", f"Process {myprocess.processid} executed completely"])
            table.add_row(
                ["State", "Running" if myprocess.state == 'R' else "Blocked"])

            print(table, '\n\n')


def run_rr_scheduling():
    process = 0
    execution = 0
    quantumsize = 0
    while process < 3 or process > 5:
        process = int(input("How many processes do you want to run? (3-5): "))
    executiontime = []

    for i in range(process):
        while execution < 1 or execution > 10:
            execution = int(
                input(f"Enter execution time of process {i + 1}: (1-10): "))
        executiontime.append(execution)
        execution = 0

    while quantumsize < 1 or quantumsize > 3:
        quantumsize = int(input("Enter your quantum size: (1-3): "))

    mypcb = PCB(process, quantumsize, executiontime)
