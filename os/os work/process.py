import random

class Process:
    def __init__(self, pid, arrival_time, burst_time, memory_required):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.memory_required = memory_required
        self.remaining_time = burst_time

    def __repr__(self):
        return (f"Process(pid={self.pid}, arrival_time={self.arrival_time}, "
                f"burst_time={self.burst_time}, memory_required={self.memory_required})")

def generate_processes(num_processes):
    processes = []
    for i in range(num_processes):
        pid = i + 1
        arrival_time = random.randint(0, 10)
        burst_time = random.randint(1, 10)
        memory_required = random.randint(10, 100)
        processes.append(Process(pid, arrival_time, burst_time, memory_required))
    return processes
