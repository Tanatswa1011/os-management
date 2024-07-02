from process import Process, generate_processes
from memory_manager import MemoryManager

def add_to_queues(processes):
    ready_queue = []
    waiting_queue = []
    for process in processes:
        if process.arrival_time == 0:
            ready_queue.append(process)
        else:
            waiting_queue.append(process)
    return ready_queue, waiting_queue

def move_waiting_to_ready(ready_queue, waiting_queue, current_time):
    for process in waiting_queue[:]:
        if process.arrival_time <= current_time:
            ready_queue.append(process)
            waiting_queue.remove(process)

def fcfs_scheduling(ready_queue, waiting_queue, memory_manager):
    ready_queue.sort(key=lambda p: p.arrival_time)
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    total_processes = len(ready_queue) + len(waiting_queue)
    memory_usage = 0
    total_burst_time = 0
    while ready_queue or waiting_queue:
        move_waiting_to_ready(ready_queue, waiting_queue, current_time)
        if not ready_queue:
            current_time += 1
            continue
        process = ready_queue.pop(0)
        if memory_manager.first_fit(process) == -1:
            print(f"Process {process.pid} cannot be allocated memory")
            continue
        print(f"Memory allocated for process {process.pid}")
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        waiting_time = current_time - process.arrival_time
        turnaround_time = waiting_time + process.burst_time
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        total_burst_time += process.burst_time
        memory_usage += process.memory_required
        print(f"Process {process.pid} is running at time {current_time}")
        current_time += process.burst_time
        memory_manager.deallocate(process)
        print(f"Memory deallocated for process {process.pid}")
    avg_waiting_time = total_waiting_time / total_processes
    avg_turnaround_time = total_turnaround_time / total_processes
    cpu_utilization = (total_burst_time / current_time) * 100
    avg_memory_utilization = memory_usage / (memory_manager.size * total_processes) * 100
    print(f"Average waiting time: {avg_waiting_time}")
    print(f"Average turnaround time: {avg_turnaround_time}")
    print(f"CPU utilization: {cpu_utilization}%")
    print(f"Average memory utilization: {avg_memory_utilization}%")

def sjf_scheduling(ready_queue, waiting_queue, memory_manager):
    ready_queue.sort(key=lambda p: (p.arrival_time, p.burst_time))
    current_time = 0
    total_waiting_time = 0
    total_turnaround_time = 0
    total_processes = len(ready_queue) + len(waiting_queue)
    memory_usage = 0
    total_burst_time = 0
    while ready_queue or waiting_queue:
        move_waiting_to_ready(ready_queue, waiting_queue, current_time)
        if not ready_queue:
            current_time += 1
            continue
        process = ready_queue.pop(0)
        if memory_manager.first_fit(process) == -1:
            print(f"Process {process.pid} cannot be allocated memory")
            continue
        print(f"Memory allocated for process {process.pid}")
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        waiting_time = current_time - process.arrival_time
        turnaround_time = waiting_time + process.burst_time
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        total_burst_time += process.burst_time
        memory_usage += process.memory_required
        print(f"Process {process.pid} is running at time {current_time}")
        current_time += process.burst_time
        memory_manager.deallocate(process)
        print(f"Memory deallocated for process {process.pid}")
    avg_waiting_time = total_waiting_time / total_processes
    avg_turnaround_time = total_turnaround_time / total_processes
    cpu_utilization = (total_burst_time / current_time) * 100
    avg_memory_utilization = memory_usage / (memory_manager.size * total_processes) * 100
    print(f"Average waiting time: {avg_waiting_time}")
    print(f"Average turnaround time: {avg_turnaround_time}")
    print(f"CPU utilization: {cpu_utilization}%")
    print(f"Average memory utilization: {avg_memory_utilization}%")

def rr_scheduling(ready_queue, waiting_queue, time_quantum, memory_manager):
    current_time = 0
    queue = ready_queue[:]
    allocated_processes = set()
    total_waiting_time = 0
    total_turnaround_time = 0
    total_processes = len(ready_queue) + len(waiting_queue)
    memory_usage = 0
    total_burst_time = 0
    failed_processes = []
    max_attempts = 10  # Maximum attempts to allocate memory

    while queue or waiting_queue:
        move_waiting_to_ready(queue, waiting_queue, current_time)
        if not queue:
            current_time += 1
            continue
        process = queue.pop(0)
        allocation_attempts = 0

        while process.pid not in allocated_processes and process not in failed_processes:
            if allocation_attempts >= max_attempts:
                print(f"Process {process.pid} cannot be allocated memory after {max_attempts} attempts, moving to failed queue.")
                failed_processes.append(process)
                break
            if memory_manager.first_fit(process) == -1:
                print(f"Process {process.pid} cannot be allocated memory, waiting...")
                allocation_attempts += 1
                continue
            print(f"Memory allocated for process {process.pid}")
            allocated_processes.add(process.pid)

        if process in failed_processes:
            continue

        if process.remaining_time > time_quantum:
            print(f"Process {process.pid} is running at time {current_time}")
            current_time += time_quantum
            process.remaining_time -= time_quantum
            queue.append(process)
        else:
            print(f"Process {process.pid} is running at time {current_time}")
            current_time += process.remaining_time
            process.remaining_time = 0
            memory_manager.deallocate(process)
            print(f"Memory deallocated for process {process.pid}")
            allocated_processes.discard(process.pid)
            turnaround_time = current_time - process.arrival_time
            waiting_time = turnaround_time - process.burst_time
            total_turnaround_time += turnaround_time
            total_waiting_time += waiting_time
            total_burst_time += process.burst_time
            memory_usage += process.memory_required
            for waiting_process in waiting_queue[:]:
                if memory_manager.first_fit(waiting_process) != -1:
                    print(f"Memory allocated for waiting process {waiting_process.pid}")
                    waiting_queue.remove(waiting_process)
                    queue.append(waiting_process)
                    allocated_processes.add(waiting_process.pid)

    avg_waiting_time = total_waiting_time / total_processes
    avg_turnaround_time = total_turnaround_time / total_processes
    cpu_utilization = (total_burst_time / current_time) * 100
    avg_memory_utilization = memory_usage / (memory_manager.size * total_processes) * 100
    print(f"Average waiting time: {avg_waiting_time}")
    print(f"Average turnaround time: {avg_turnaround_time}")
    print(f"CPU utilization: {cpu_utilization}%")
    print(f"Average memory utilization: {avg_memory_utilization}%")
    if failed_processes:
        print(f"Failed processes: {[process.pid for process in failed_processes]}")

def simulate_scheduling(processes, algorithm, memory_manager, time_quantum=None):
    ready_queue, waiting_queue = add_to_queues(processes)
    if algorithm == 'FCFS':
        fcfs_scheduling(ready_queue, waiting_queue, memory_manager)
    elif algorithm == 'SJF':
        sjf_scheduling(ready_queue, waiting_queue, memory_manager)
    elif algorithm == 'RR' and time_quantum is not None:
        rr_scheduling(ready_queue, waiting_queue, time_quantum, memory_manager)
    else:
        print("Invalid algorithm or missing time quantum for Round Robin")
