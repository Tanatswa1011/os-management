class MemoryManager:
    def __init__(self, size):
        self.size = size
        self.memory = [0] * size

    def first_fit(self, process):
        start = -1
        for i in range(self.size):
            if self.memory[i] == 0:
                if start == -1:
                    start = i
                if i - start + 1 == process.memory_required:
                    for j in range(start, i + 1):
                        self.memory[j] = process.pid
                    return start
            else:
                start = -1
        return -1

    def deallocate(self, process):
        for i in range(self.size):
            if self.memory[i] == process.pid:
                self.memory[i] = 0
