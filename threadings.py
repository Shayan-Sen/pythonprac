"""
Implementation of basic threading
"""

import threading


def print_numbers():
    for i in range(10):
        print(f"Thread: {threading.current_thread().name} → {i}")


t1 = threading.Thread(target=print_numbers, name="Thread-1")
t2 = threading.Thread(target=print_numbers, name="Thread-2")

t1.start()
t2.start()

t1.join()
t2.join()

print("Main thread execution completed!")
