from time import sleep
from threading import Thread, Lock


class Account(object):
    def __init__(self):
        self._balance = 0    # 初始化金额
        self._lock = Lock()  # 设置锁(Lock)

    def deposit(self, money):
        self._lock.acquire()   # 获取锁
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            self._lock.release()  # 释放锁

    @property
    def balance(self):
        return self._balance


class AddMoney(Thread):
    def __init__(self, accout, money):
        super().__init__()
        self._accout = accout
        self._money = money

    def run(self):
        self._accout.deposit(self._money)


def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoney(account, 1) # 每次循环会产生新的线程
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为：¥%.2f元' % account.balance)


if __name__ == '__main__':
    main()
