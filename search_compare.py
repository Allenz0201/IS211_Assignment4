import time
import random

TARGET = 99_999_999


def get_random_list(n):
    a = list(range(1, n + 1))
    random.shuffle(a)
    return a


def sequential_search(a_list, item):
    start = time.time()
    found = False
    for x in a_list:
        if x == item:
            found = True
            break
    elapsed = time.time() - start
    return found, elapsed


def ordered_sequential_search(a_list, item):
    start = time.time()
    found = False
    for x in a_list:
        if x == item:
            found = True
            break
        if x > item:
            break
    elapsed = time.time() - start
    return found, elapsed


def binary_search_iterative(a_list, item):
    start = time.time()
    first, last = 0, len(a_list) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if a_list[mid] == item:
            found = True
        elif item < a_list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    elapsed = time.time() - start
    return found, elapsed


def binary_search_recursive(a_list, item):
    def _bs(lst, target):
        if not lst:
            return False
        mid = len(lst) // 2
        if lst[mid] == target:
            return True
        if target < lst[mid]:
            return _bs(lst[:mid], target)
        return _bs(lst[mid + 1:], target)

    start = time.time()
    found = _bs(a_list, item)
    elapsed = time.time() - start
    return found, elapsed


def benchmark_once(n):
    base = get_random_list(n)

    # Sequential: unsorted
    _, t_seq = sequential_search(base, TARGET)

    # Ordered sequential: needs sorted
    sorted1 = sorted(base)
    _, t_ord = ordered_sequential_search(sorted1, TARGET)

    # Binary iterative
    sorted2 = sorted(base)
    _, t_bi = binary_search_iterative(sorted2, TARGET)

    # Binary recursive
    sorted3 = sorted(base)
    _, t_br = binary_search_recursive(sorted3, TARGET)

    return t_seq, t_ord, t_bi, t_br


def main():
    sizes = [500, 1000, 5000]
    trials = 100

    for n in sizes:
        total_seq = total_ord = total_bi = total_br = 0.0
        for _ in range(trials):
            t_seq, t_ord, t_bi, t_br = benchmark_once(n)
            total_seq += t_seq
            total_ord += t_ord
            total_bi += t_bi
            total_br += t_br

        avg_seq = total_seq / trials
        avg_ord = total_ord / trials
        avg_bi = total_bi / trials
        avg_br = total_br / trials

        print(f"\nList size {n}")
        print(f"Sequential Search took {avg_seq:10.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {avg_ord:10.7f} seconds to run, on average")
        print(f"Binary Search Iterative took {avg_bi:10.7f} seconds to run, on average")
        print(f"Binary Search Recursive took {avg_br:10.7f} seconds to run, on average")


if __name__ == "__main__":
    main()
