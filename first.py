class BankersAlgorithm:
    def __init__(self, num_processes, num_resources, total_resources, max_matrix, allocation_matrix):
        self.num_processes = num_processes
        self.num_resources = num_resources
        self.total_resources = total_resources
        self.max_matrix = max_matrix
        self.allocation_matrix = allocation_matrix
        self.available = [total_resources[j] - sum(allocation_matrix[i][j] for i in range(num_processes)) for j in range(num_resources)]
        self.need_matrix = self.calculate_need()

    def calculate_need(self):
        return [[self.max_matrix[i][j] - self.allocation_matrix[i][j] for j in range(self.num_resources)] for i in range(self.num_processes)]

    def is_safe_state(self):
        work = self.available[:]
        finish = [False] * self.num_processes
        safe_sequence = []

        print("\nAvailable Resources:", self.available)
        print("Allocated || Max || Need")
        for i in range(self.num_processes):
            print(f"{self.allocation_matrix[i]} | {self.max_matrix[i]} | {self.need_matrix[i]}")

        while len(safe_sequence) < self.num_processes:
            found_process = False
            for i in range(self.num_processes):
                if not finish[i] and all(self.need_matrix[i][j] <= work[j] for j in range(self.num_resources)):
                    work = [work[j] + self.allocation_matrix[i][j] for j in range(self.num_resources)]
                    finish[i] = True
                    safe_sequence.append(i)
                    print(f"\nProcess {i+1} completed")
                    print("Available matrix:", work)
                    print("Allocated || Max || Need")
                    for k in range(self.num_processes):
                        if finish[k]:
                            print(f"{[0] * self.num_resources} | {self.max_matrix[k]} | {[0] * self.num_resources}")
                        else:
                            print(f"{self.allocation_matrix[k]} | {self.max_matrix[k]} | {self.need_matrix[k]}")
                    found_process = True
                    break
            
            if not found_process:
                print("\nThe system is not in a safe state!")
                return False

        print("\nThe system is in a safe state!")
        return True


num_processes = int(input("Enter number of processes: "))
num_resources = int(input("Enter number of resources: "))

print("Enter total number of each resource:")
total_resources = list(map(int, input().split()))

print("Enter Max resources for each process:")
max_matrix = [list(map(int, input(f"For process {i + 1}: ").split())) for i in range(num_processes)]

print("Enter allocated resources for each process:")
allocation_matrix = [list(map(int, input(f"For process {i + 1}: ").split())) for i in range(num_processes)]

banker = BankersAlgorithm(num_processes, num_resources, total_resources, max_matrix, allocation_matrix)
banker.is_safe_state()
