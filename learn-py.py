import threading
import time

def job1():
    time.sleep(1)
    print("Job1 finished")

def job2():
    time.sleep(2)
    print("Job2 finished")

def job3():
    time.sleep(3)
    print("Job3 finished")

def job4(x):
    time.sleep(x)
    print("Job4 finished")

x = threading.Thread(target=job1, name='Job1')
y = threading.Thread(target=job2, name='Job2')
z = threading.Thread(target=job3, name='Job3')
a = threading.Thread(target=job4, name='Job4', args=(1,))

x.start()
y.start()
z.start()
a.start()

x.join()
y.join()
z.join()
# a.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter()) # time since the process started