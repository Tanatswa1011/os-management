import argparse
from process import Process
from memory_manager import MemoryManager
from scheduler import simulate_scheduling

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process Scheduling and Memory Management Simulation')
    parser.add_argument('num_processes', type=int, help='Number of processes')
    parser.add_argument('--algorithm', choices=['FCFS', 'SJF', 'RR'], required=True, help='Scheduling algorithm')
    parser.add_argument('--time_quantum', type=int, help='Time quantum for Round Robin scheduling', default=2)
    parser.add_argument('--memory_size', type=int, default=100, help='Size of memory for memory management')

    return parser.parse_args()

def main():
    args = parse_arguments()

    processes = []
    for i in range(args.num_processes):
        pid = i + 1
        print(f"Enter details for process {pid}:")
        arrival_time = int(input("Arrival time: "))
        burst_time = int(input("Burst time: "))
        memory_required = int(input("Memory required: "))
        processes.append(Process(pid, arrival_time, burst_time, memory_required))

    memory_manager = MemoryManager(args.memory_size)

    print("\nRunning simulation...\n")
    simulate_scheduling(processes, args.algorithm, memory_manager, args.time_quantum)
    print("\nSimulation completed.")

if __name__ == "__main__":
    main()


# CLI Command: python main.py 5 --algorithm RR --time_quantum 2 --memory_size 100

# python main.py: This part tells the Python interpreter to execute the main.py script.
#
# 5: This is a positional argument that specifies the number of processes to simulate. In this case, the user wants to simulate 5 processes.
#
# --algorithm RR: This is an optional argument that specifies which scheduling algorithm to use. The --algorithm flag indicates that the next value (RR) is the selected algorithm. RR stands for Round Robin scheduling.
#
# --time_quantum 2: This is another optional argument specific to the Round Robin (RR) scheduling algorithm. The --time_quantum flag indicates that the next value (2) is the time quantum, which is the maximum time a process can run before the scheduler moves on to the next process in the queue. This argument is only required for Round Robin scheduling.
#
# --memory_size 100: This optional argument specifies the size of the memory to be used in the simulation. The --memory_size flag indicates that the next value (100) is the total memory size available for processes.