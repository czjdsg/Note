# 小根堆向下调整函数
def sift(li, low, high):
    i = low
    j = 2 * i + 1
    tmp = li[i]
    while j <= high:
        if j+1 <= high and li[j] > li[j+1]:
            j += 1
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp

def topk(li, k):
    heap = li[0:k]
    # 对前k个元素建小根堆
    for i in range((k-2)//2, -1, -1):
        sift(heap, i, k-1)
    # 遍历
    for j in range(k, len(li)):
        if li[j] > heap[0]:
            heap[0] = li[j]
            sift(heap, 0, k-1)
    # 依次出数
    for i in range(k-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i-1)
    return heap
import random
li = [i for i in range(100)]
random.shuffle(li)
print(topk(li, 10))
