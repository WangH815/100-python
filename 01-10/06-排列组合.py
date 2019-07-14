M = int(input('请输入M：'))
N = int(input('请输入N：'))

if M < 1 or N <1 or M <= N:
    print('输入非法...')

fn = fm = fmn = 1
for i in range(1, M + 1):
    fm *= i

for i in range(1, N + 1):
    fn *= i

for i in range(1, M - N + 1):
    fmn *= i

print(fm / (fn * fmn))
