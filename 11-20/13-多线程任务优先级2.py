from multiprocessing import Process, Queue
from time import time


def task_handler(curr_list, result_queue):
    total = 0
    for num in curr_list:
        total += num
    result_queue.put(total)


def main():
    process = []
    num_list = [x for x in range(1, 100000001)]
    result_queue = Queue()
    index = 0
    ts = 20
    part = 100000000 // ts
    for _ in range(ts):
        p = Process(target=task_handler,
                    args=(num_list[index:index + part], result_queue))
        index += part
        process.append(p)
        p.start()

    start = time()
    for p in process:
        p.join()
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('Exec times:%.2f' % (end - start))


if __name__ == '__main__':
    main()
