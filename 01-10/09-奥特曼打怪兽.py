from abc import ABCMeta, abstractmethod
from random import randint, randrange

'''战斗者类'''
class Fighter(object, metaclass=ABCMeta):
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod  # 定义抽象方法，由子类实现
    def attack(self, other):
        pass  # 占位


class Ultraman(Fighter):
    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp, mp):
        super().__init__(name, hp)  # 调用超类初始化方法
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, others):
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        incr_point = randint(1, 10)
        self._mp += incr_point
        return incr_point

    def __str__(self):  # 重写 __str__() 方法
        return '%s奥特曼: \n' % self._name + \
               '生命值：%d\n' % self._hp + \
               '魔法值：%d\n' % self._mp


class Moster(Fighter):
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '%s: ' % self._name + '生命值：%d\n' % self._hp


def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False


def select_alive_one(mosters):
    mosters_len = len(mosters)
    while True:
        index = randrange(mosters_len)
        moster = mosters[index]
        if moster.alive > 0:
            return moster


def display_info(ultraman, mosters):
    print(ultraman)
    for moster in mosters:
        print(moster, end='')


def main():
    u = Ultraman('赛文', 500, 12)
    m1 = Moster('怪兽1', 160)
    m2 = Moster('怪兽2', 200)
    m3 = Moster('怪兽3', 180)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('============第 %02d 回合==========' % fight_round)
        m = select_alive_one(ms)
        skill = randint(1, 10)
        if skill <= 6:
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        elif skill <= 9:
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败.' % u.name)
        else:
            if u.huge_attack(m):
                print('%s使用了究极必杀技虐了%s' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        if m.alive > 0:
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)
        fight_round += 1
    print('\n============战斗结束！==========')
    if u.alive > 0:
        print('%s奥特曼胜利！' % u.name)
    else:
        print('小怪兽胜利！')


if __name__ == '__main__':
    main()
