import threading
import time


# Function to be executed in the thread
def print_numbers():
    for i in range(5):
        time.sleep(1)  # Simulating some work
        print(f"Thread 1: {i}")


def print_letters():
    for letter in "abcde":
        time.sleep(1)  # Simulating some work
        print(f"Thread 2: {letter}")


# Create two threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start the threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print("Done!")
