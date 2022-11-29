import random
for i in range(-10, 10):
    random.seed(i)
    print(f'{i}) {random.randint(1,9)}')
print(random.getstate())