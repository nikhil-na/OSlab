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
        print("Allocated | Max | Need")
        for i in range(self.num_processes):
            print(f"{self.allocation_matrix[i]} | {self.max_matrix[i]} | {self.need_matrix[i]}")

        while len(safe_sequence) < self.num_processes:
            found_process = False
            for i in range(self.num_processes):
                if not finish[i] and all(self.need_matrix[i][j] <= work[j] for j in range(self.num_resources)):
                    # Simulate resource allocation to process i
                    work = [work[j] + self.allocation_matrix[i][j] for j in range(self.num_resources)]
                    finish[i] = True
                    safe_sequence.append(i)
                    print(f"\nProcess {i+1} completed")
                    print("Available matrix:", work)
                    print("Allocated | Max | Need")
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

    def request_resources(self, process_num, request):
        if any(request[j] > self.need_matrix[process_num][j] for j in range(self.num_resources)):
            print("Error: Process has exceeded its maximum claim.")
            return False

        if any(request[j] > self.available[j] for j in range(self.num_resources)):
            print("Resources are not available to fulfill the request at this time.")
            return False

        # Temporarily allocate resources
        original_available = self.available[:]
        original_allocation = self.allocation_matrix[process_num][:]
        original_need = self.need_matrix[process_num][:]

        self.available = [self.available[j] - request[j] for j in range(self.num_resources)]
        self.allocation_matrix[process_num] = [self.allocation_matrix[process_num][j] + request[j] for j in range(self.num_resources)]
        self.need_matrix[process_num] = [self.need_matrix[process_num][j] - request[j] for j in range(self.num_resources)]

        if self.is_safe_state():
            print(f"\nResources granted to Process {process_num + 1}.")
            return True
        else:
            print("The request would leave the system in an unsafe state, rolling back.")
            # Back to original state
            self.available = original_available
            self.allocation_matrix[process_num] = original_allocation
            self.need_matrix[process_num] = original_need
            return False

def main():
    num_processes = int(input("Enter number of processes: "))
    num_resources = int(input("Enter number of resources: "))

    print("Enter total number of each resource:")
    total_resources = list(map(int, input().split()))

    print("Enter Max resources for each process:")
    max_matrix = [list(map(int, input(f"For process {i + 1}: ").split())) for i in range(num_processes)]

    print("Enter allocated resources for each process:")
    allocation_matrix = [list(map(int, input(f"For process {i + 1}: ").split())) for i in range(num_processes)]

    banker = BankersAlgorithm(num_processes, num_resources, total_resources, max_matrix, allocation_matrix)

    while True:
        print("\nChoose an option:")
        print("1. Check system's safe state (Safety Algorithm)")
        print("2. Make a resource request (Resource Request Algorithm)")
        print("3. Exit")
        choice = int(input("Enter choice: "))

        if choice == 1:
            banker.is_safe_state()
        elif choice == 2:
            process_num = int(input("Enter the process number (1-based index): ")) - 1
            request = list(map(int, input("Enter the resources to request: ").split()))
            banker.request_resources(process_num, request)
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
