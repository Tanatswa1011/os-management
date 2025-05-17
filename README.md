# 🖥️ Process Scheduling and Memory Management Simulation

This project simulates core concepts in Operating System design — specifically, **CPU scheduling algorithms** and **memory management strategies** — using a command-line interface for easy interaction and testing.

## 📌 Features

- Implementation of **CPU Scheduling Algorithms**:
  - **First-Come, First-Served (FCFS)**
  - **Shortest Job First (SJF)**
  - **Round Robin (RR)**

- Simulation of **Memory Management** using:
  - **First-Fit Allocation Strategy**

## 📊 Key Takeaways

- **FCFS** is simple and intuitive, but can lead to **long wait times for shorter tasks**, especially when long processes arrive first.
- **SJF** optimizes for low average waiting time by prioritizing shorter tasks, but risks **starvation of longer processes**.
- **RR** ensures fairness by giving each process equal time slices, but introduces **context-switching overhead**, potentially reducing performance.

- The **First-Fit memory allocation** strategy was effective in this simulation, but highlighted the need for **sufficient contiguous memory**. Fragmentation can limit efficiency and resource utilization.

## 📈 Conclusion

The project demonstrates that the choice of **scheduling algorithm** and **memory management strategy** has a **significant impact on system performance**. Understanding trade-offs between fairness, efficiency, and complexity is key when designing or evaluating an operating system.

## 🛠️ Tech Stack

- Language: Python  
- Interface: Command-Line (CLI)  
- Topics: Scheduling, Memory Management, Operating Systems

## 🚀 Getting Started

Clone the repo and compile the C++ source files to test different scheduling and memory allocation strategies in a simulated environment.

```bash
git clone https://github.com/your-username/os-scheduler-simulation.git
cd os-scheduler-simulation
g++ -o simulator main.cpp
./simulator
