def expand(*args, sep=' '):
    s_ans = ''
    for index in range(len(args)):
        s_ans += args[index]
    count = [s_ans for _ in range(len(args))]
    # print(f'{count=}')
    s_ans = sep.join(count)
    # print(f'{s=}')
    return 'Ans >>> ' + s_ans

def check():
    nums = [1, 2, 3, 4, 5]
    print(nums[::-2])
    print(nums[2:5])
    print(nums[4::-2])
    print(nums[2::5])
    print(nums[-1::-3])
    print(nums[:-2])

a = [[0 for _ in range(51)] for _ in range(51)]
# print(a, len(a), len(a[1]), sep='\n')
n = 50
for j in range(50, 0, -1):
    k = j
    for i in range(n, 0, -1):
        if n - i + 1 <= j:
            a[i][j] = k
            k += 1
        else:
            a[i][j] = 0
j = 20
s = 0
for i in range(1, n + 1):
    s += a[i][j]
print(s)

p = 1
k = 21
while k < 29:
    p *= (26 - k)
    k += 2
print(p)

print(expand('bee', 'geek', sep='!'))
print(expand('Ti', 'mur', sep=' Guev '))
print(expand())
print(expand(sep='Hello!'))
print(expand('A', 'B', 'C', sep='!'))  # ВЫВОД: ABC!ABC!ABC
print(expand('Timur', 'Arthur', 'Valera'))  # ВЫВОД: TimurArthurValera TimurArthurValera TimurArthurValera

print('\tDone!')
check()