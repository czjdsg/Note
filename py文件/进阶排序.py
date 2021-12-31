#---------------------------------快速排序-----------------------------------
def partition(li, left, right):
    tmp = li[left] #取出左边第一个数
    while left < right:
        while left < right and li[right] >= tmp: #从右边找一个比tmp小的数
            right -= 1
        li[left] = li[right] #找出的值写入左边的空位上
        while left < right and li[left] <= tmp: #从左边找一个比tmp大的数
            left += 1
        li[right] = li[left] #找出的值写入右边的空位上
    li[left] = tmp #最初找出的值写到最终的空位上
    return left #返回mid的值(将在Quick_sort函数中使用)

def Quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        Quick_sort(li, left, mid-1)
        Quick_sort(li, mid+1, right)
li = [8,4,4,2,6,8,6,3,5,7,87,43,4,5,2]
Quick_sort(li, 0, len(li)-1)
print(li)

#---------------------------------堆排序-----------------------------------
def sift(li, low, high): #调整函数(假设节点左右子树都是堆，但自身不是堆)
    i = low #i最开始指向根节点
    j = 2 * i + 1 #左孩子
    tmp = li[low] #把堆顶存起来
    while j <= high: #只要j位置有数
        if j + 1 <= high and li[j+1] > li[j]: # 如果右孩子比左孩子大且右孩子不越界
            j = j + 1
        if tmp < li[j]:
            li[i] = li[j]
            i = j #往下看一层，更新 i,j
            j = 2 * i + 1
#-------------------------------------------------------------------------------
        else:                                                       #可整体写为       else:
            li[i] = tmp #将tmp放到某一级领导的位置上，跳出循环                              break
            break                                                   #            li[i] = tmp
    else:
        li[i] = tmp #将tmp放到一个最低级的位置上，跳出循环
# -------------------------------------------------------------------------------
def Heap_sort(li):
    #先构造堆
    n = len(li)
    for i in range((n-2)//2, -1, -1): #遍历每一个待调整的父节点(从下往上)
        sift(li, i, n-1) #high仅有一个作用，就是判断j是否越界，故n-1就够用了
    #建堆完成
    #开始排序
    for i in range(n-1, -1, -1): #i指向当前堆的最后一个元素
        li[0], li[i] = li[i], li[0] #将最大的元素排在末尾
        sift(li, 0, i-1) #向下调整一次
#---------------------------------归并排序-----------------------------------
def Merge_sort(li, low, mid, high):
    i = low
    j = mid + 1 # i,j表示两个有序表的第一个元素的下标
    Ltmp = []
    while i <= mid and j <= high: # 只要左右两边都有数
         if li[i] < li[j]:
            Ltmp.append(li[i])
            i += 1
         else:
             Ltmp.append(li[j])
             j += 1
    # 当一边列表全部取完之后，将另一边剩下的所有元素
    while i <= mid:
        Ltmp.append(li[i])
        i += 1
    while j <= high:
        Ltmp.append(li[j])
        j += 1
    li[low:high+1] = Ltmp




#---------------------------------快速排序-----------------------------------

