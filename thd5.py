import threading
import os

sum_result = []
def compute_sum(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        line = file.read()
        numbers = map(int, line.split(','))
        total_sum = sum(numbers)
    sum_result.append(total_sum)

def main():
    file_paths = ['file1.txt', 'file2.txt', 'file3.txt']
    threads = []
    for file_path in file_paths:
        thread = threading.Thread(target=compute_sum, args=(file_path,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    print(sum(sum_result))

if __name__ == '__main__':
    main()