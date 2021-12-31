def hanoi(n, a, b, c):#n个盘子从a经b移动到c
    if n > 0:
        hanoi(n-1, a, c, b)
        print("从"+a+"移动到"+c)
        hanoi(n-1, b, a, c)

hanoi(4, 'A', 'B', 'C')
