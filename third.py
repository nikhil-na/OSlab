class DeadlockDetector:
    def __init__(self, num_processes, num_resources, available, allocation_matrix, request_matrix):
        self.num_processes = num_processes
        self.num_resources = num_resources
        self.available = available
        self.allocation_matrix = allocation_matrix
        self.request_matrix = request_matrix
        self.finish = [False] * num_processes

    def detect_deadlock(self):
        work = self.available[:]
        deadlocked_processes = []

        print("\nInitial Available Resources:", self.available)
        print("Allocated | Request")
        for i in range(self.num_processes):
            print(f"Process {i + 1}: {self.allocation_matrix[i]} | {self.request_matrix[i]}")

        # Find processes that can complete
        while True:
            found_process = False
            for i in range(self.num_processes):
                if not self.finish[i] and all(self.request_matrix[i][j] <= work[j] for j in range(self.num_resources)):
                    # Process i can complete and release resources
                    work = [work[j] + self.allocation_matrix[i][j] for j in range(self.num_resources)]
                    self.finish[i] = True
                    found_process = True
                    print(f"\nProcess {i + 1} can complete and release resources.")
                    print("Updated Available Resources:", work)
                    break

            if not found_process:
                break

        # Determine deadlocked processes
        deadlocked_processes = [i + 1 for i in range(self.num_processes) if not self.finish[i]]

        if deadlocked_processes:
            print("\nThe system is in a deadlock.")
            print("Deadlocked Processes:", deadlocked_processes)
        else:
            print("\nThe system is deadlock-free.")

        return deadlocked_processes

def main():
    num_processes = int(input("Enter the number of processes: "))
    num_resources = int(input("Enter the number of resources: "))

    print("Enter the available resources:")
    available = list(map(int, input().split()))

    print("Enter the allocation matrix for each process:")
    allocation_matrix = [list(map(int, input(f"For process {i + 1}: ").split())) for i in range(num_processes)]

    print("Enter the request matrix for each process:")
    request_matrix = [list(map(int, input(f"For process {i + 1}: ").split())) for i in range(num_processes)]

    detector = DeadlockDetector(num_processes, num_resources, available, allocation_matrix, request_matrix)
    detector.detect_deadlock()

if __name__ == "__main__":
    main()
