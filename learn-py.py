from multiprocessing import Process, cpu_count
import time

def foo(name):
    print('hello', name)

def main():
    print(f"Number of CPU cores: {cpu_count()}")
    x = Process(target=foo, args=("10k",))

    x.start()
    x.join()

    print(time.perf_counter())


if __name__ == '__main__':
    main()