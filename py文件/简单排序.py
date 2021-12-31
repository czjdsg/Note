#---------------------------冒泡排序--------------------------------
def Bubble_sort(li):
    for i in range(0, len(li)-1): #循环趟数，每趟可以排出一个最大数
        exchange = False
        for j in range(0, len(li)-i-1): #每趟需要交换多少次
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            return
li = [2,3,2,65,75,3,2,345,64,7877]
Bubble_sort(li)
print(li)
#---------------------------选择排序--------------------------------
def Select_sort_simple(li):
    li_new = []
    for i in range(0, len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new

def Select_sort(li):
    for i in range(0, len(li)-1): #第i趟
        min_loc = i
        for j in range(i+1, len(li)): #加1是为了不和自己比，节约一次
            if li[min_loc] > li[j]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]

#---------------------------插入排序--------------------------------
def Insert_sort(li):
    for i in range(1, len(li)): #i 表示待插入数字的下标
        j = i - 1
        tmp = li[i]
        while li[j] > tmp and j >= 0:
            li[j+1] = li[j]
            j -= 1
        li[j+1] = tmp

li = [3,4,5,2,4,6,4,7,9]
Insert_sort(li)
print(li)
