import time
import random


def get_random_list(n):
    a = list(range(1, n + 1))
    random.shuffle(a)
    return a


def insertion_sort(a_list):
    lst = a_list[:]  # working on a copy
    start = time.time()
    for i in range(1, len(lst)):
        cur = lst[i]
        j = i
        while j > 0 and lst[j - 1] > cur:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = cur
    return time.time() - start


def shell_sort(a_list):
    lst = a_list[:]
    gap = len(lst) // 2
    start = time.time()
    while gap > 0:
        for i in range(gap, len(lst)):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return time.time() - start


def python_sort(a_list):
    lst = a_list[:]
    start = time.time()
    lst.sort()
    return time.time() - start


def benchmark_once(n):
    base = get_random_list(n)
    t_py = python_sort(base)
    t_ins = insertion_sort(base)
    t_shell = shell_sort(base)
    return t_ins, t_shell, t_py


def main():
    sizes = [500, 1000, 5000]
    trials = 100

    for n in sizes:
        total_ins = total_shell = total_py = 0.0
        for _ in range(trials):
            t_ins, t_shell, t_py = benchmark_once(n)
            total_ins += t_ins
            total_shell += t_shell
            total_py += t_py

        avg_ins = total_ins / trials
        avg_shell = total_shell / trials
        avg_py = total_py / trials

        print(f"\nList size {n}")
        print(f"Insertion Sort took {avg_ins:10.7f} seconds to run, on average")
        print(f"Shell Sort took {avg_shell:10.7f} seconds to run, on average")
        print(f"Python Sort took {avg_py:10.7f} seconds to run, on average")


if __name__ == "__main__":
    main()
