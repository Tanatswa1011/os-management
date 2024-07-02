from process import Process
from memory_manager import MemoryManager
from scheduler import simulate_scheduling

def test_scheduler():
    # Basic functionality test cases
    test_cases = [
        {
            "description": "Basic FCFS",
            "num_processes": 5,
            "processes": [Process(1, 0, 4, 20), Process(2, 1, 3, 30), Process(3, 2, 5, 40), Process(4, 3, 2, 10), Process(5, 4, 1, 50)],
            "algorithm": "FCFS",
            "time_quantum": None
        },
        {
            "description": "Basic SJF",
            "num_processes": 5,
            "processes": [Process(1, 0, 4, 20), Process(2, 1, 3, 30), Process(3, 2, 5, 40), Process(4, 3, 2, 10), Process(5, 4, 1, 50)],
            "algorithm": "SJF",
            "time_quantum": None
        },
        {
            "description": "Basic RR",
            "num_processes": 5,
            "processes": [Process(1, 0, 4, 20), Process(2, 1, 3, 30), Process(3, 2, 5, 40), Process(4, 3, 2, 10), Process(5, 4, 1, 50)],
            "algorithm": "RR",
            "time_quantum": 2
        },
        # Edge case test: all processes arriving at the same time
        {
            "description": "All processes arrive at the same time",
            "num_processes": 3,
            "processes": [Process(1, 0, 2, 10), Process(2, 0, 1, 20), Process(3, 0, 3, 30)],
            "algorithm": "FCFS",
            "time_quantum": None
        },
        # Edge case test: processes with zero burst time
        {
            "description": "Processes with zero burst time",
            "num_processes": 3,
            "processes": [Process(1, 0, 0, 10), Process(2, 1, 0, 20), Process(3, 2, 0, 30)],
            "algorithm": "SJF",
            "time_quantum": None
        },
        # Edge case test: memory requirement exceeding available memory
        {
            "description": "Memory requirement exceeds available memory",
            "num_processes": 3,
            "processes": [Process(1, 0, 2, 200), Process(2, 1, 1, 300), Process(3, 2, 3, 400)],
            "algorithm": "RR",
            "time_quantum": 2
        },
        # Varying arrival patterns
        {
            "description": "Varying arrival patterns",
            "num_processes": 4,
            "processes": [Process(1, 0, 4, 20), Process(2, 5, 3, 30), Process(3, 7, 5, 40), Process(4, 10, 2, 10)],
            "algorithm": "FCFS",
            "time_quantum": None
        },
        # Varying burst times
        {
            "description": "Varying burst times",
            "num_processes": 4,
            "processes": [Process(1, 0, 1, 20), Process(2, 1, 10, 30), Process(3, 2, 5, 40), Process(4, 3, 3, 10)],
            "algorithm": "SJF",
            "time_quantum": None
        },
        # Varying memory requirements
        {
            "description": "Varying memory requirements",
            "num_processes": 4,
            "processes": [Process(1, 0, 4, 20), Process(2, 1, 3, 300), Process(3, 2, 5, 40), Process(4, 3, 2, 500)],
            "algorithm": "RR",
            "time_quantum": 2
        }
    ]

    for case in test_cases:
        print(f"Testing: {case['description']}")
        memory_manager = MemoryManager(100)
        simulate_scheduling(case['processes'], case['algorithm'], memory_manager, case['time_quantum'])
        print()

if __name__ == "__main__":
    test_scheduler()


# test 2 and 4 are supposed to fail because they are designed to demand more memory than the process has
