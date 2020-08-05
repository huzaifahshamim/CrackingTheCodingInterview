import numpy as np


def AntCrawl(K):
    initial = 'right'
    #LET 0 be WHITE and 1 be BLACK
    steps = 0
    t_r = {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}
    t_l = {'up': 'left', 'left': 'down', 'down': 'right', 'right': 'up'}
    iterate = {'up': [-1, 0], 'right': [0, 1], 'left': [0, -1], 'down': [1, 0]}
    grid = np.random.randint(0, 2, [K, K])
    [x, y] = (np.random.randint(0, K), np.random.randint(0, K))
    print(grid)
    print(x, y)
    while steps <= K:
        if grid[x, y] == 0:
            grid[x, y] == 1
            initial = t_r[initial]
            x += iterate[initial][0]
            y += iterate[initial][1]
        else:
            grid[x, y] == 0
            initial = t_l[initial]
            x += iterate[initial][0]
            y += iterate[initial][1]
        steps += 1

    print(grid)


AntCrawl(5)
