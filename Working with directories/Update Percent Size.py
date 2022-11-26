import random


def main():
    d = dict()
    for i in range(3):
        d[str(i)] = random.randint(1, 10)
        for j in range(3, 5):
            d[str(i) + str(j)] = random.randint(1, 10)

    print('D:', d)
    print('len(D):', len(d), '\n')

    print('\tStarted dict:')
    for key, item in d.items():
        print(f'\t{key:3}: {item:3}')
    print()

    for path, size in d.items():
        t_size = 0
        for item in d:
            if item != path and path in item:
                t_size += d[item]
                print(f'path: {path}, item: {item}, t_size: {t_size}')
        if t_size != 0:
            d[path] = (size, size + t_size)
            print(f'd[{path}] = {d[path]}')

    print('\n\tNew dict:')
    for key, item in d.items():
        print(f'\t{key:3}: {item}')
    print()


if __name__ == '__main__':
    main()
