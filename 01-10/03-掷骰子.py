from random import randint

face = randint(1,5)

if face == 1:
    result = '唱歌'
elif face == 2:
    result = '跳舞'
else:
    result = '讲笑话'

print(result)