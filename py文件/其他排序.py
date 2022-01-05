# ---------------------------------希尔排序-----------------------------------
def Insert_sort_gap(li, gap):
    for i in range(gap, len(li)):
        j = i - gap
        tmp = li[i]
        while tmp < li[j] and j >= 0:
            li[j+gap] = li[j]
            j -= gap
        li[j+gap] = tmp

def Shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        Insert_sort_gap(li, d)
        d //= 2

# ---------------------------------计数排序-----------------------------------
def Count_sort(li, max_count=100):
    count = [0 for i in range(max_count+1)] # 创建一个长度为max_count+1，值全部为0的列表
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)

# ---------------------------------桶排序-----------------------------------
def Bucket_sort(li, n=100, max_number=10000): # n表示一共有多少个桶
    buckets = [[] for i in range(n)] # 创建n个桶，并放入一个列表
    for val in li:
        i = min(val // (max_number // n), n-1) # i表示val放到几号桶里，运用min是为了防止i超过n-1
        # 把val加入对应的桶里而且对桶内进行排序
        buckets[i].append(val)
        j = len(buckets[i]) - 2
        while buckets[i][j+1] < buckets[i][j] and j >= 0:
            buckets[i][j+1], buckets[i][j] = buckets[i][j], buckets[i][j+1]
            j -= 1
    # 最后把每一个排好的桶合并起来
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)
    return sorted_li

# import random
#
# li = [random.randint(0,10000) for i in range(100000)]
# print(Bucket_sort(li))

# ---------------------------------基数排序-----------------------------------
def Radix_sort(li):
    max_num = max(li)
    it = 0 # 迭代次数
    while 10 ** it <= max_num:
        buckets = [[] for i in range(10)]
        for val in li:
            digit = (val // 10 ** it) % 10 # 取出val从右向左数的第(it + 1)位
            buckets[digit].append(val)
        li.clear()
        for buc in buckets:
            li.extend(buc) # 把数重新写回li，完成一次迭代
        it += 1

# import random
#
# li = [random.randint(0,10000) for i in range(100000)]
# Radix_sort(li)
# print(li)
