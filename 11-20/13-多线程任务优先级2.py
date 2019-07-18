from multiprocessing import Process, Queue
from random import randint
from time import time


def task_handler(curr_list, result_queue):
    totol = 0
    for num in curr_list:
        totol += num
    result_queue.put(totol)


def main():
    process = []
    num_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    for _ in range(8):
        p = Process(target=task_handler,
                    args=(num_list[index:index + 12500000], result_queue))
        index += 12500000
        process.append(p)
        p.start()

    start = time()
    for p in process:
        p.join()
    totol = 0
    while not result_queue.empty():
        totol += result_queue.get()
    print(totol)
    end = time()
    print('Exec times:%.2f' % (end - start))


if __name__ == '__main__':
    main()
