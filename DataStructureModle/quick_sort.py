"""
快速排序
1.从数数列中挑选出一个元素，称为”基准“
2.重新排序数列，所有元素比基准小的摆放在基准前面，所有元素比基准值大的摆放在基准的后面（相同的数据可以放到任一边）在这个分区退出之后，该基准就是处于数列中间的位置，这成为分区操作
3.递归地把小于基准的元素的子数列和大于基准值元素的子数列排序
o(nlogn) o(n2) o(nlogn) o(nlogn) 不稳定
"""
def quick_sort(list1):
    #此函数完成分区操作
    def partition(arr,left,right):
        key = left #划分参考数索引，默认第一个数为基准数 可以优化
        while left < right:
            #如果列表后边的数，比基准数大或者相等，则前移以为知道有比基准数小的数出现
            while left < right and arr[right] >= arr[key]:
                right -= 1
            #如果列表前边的数据，比基准值小或者相等，则后移一位知道有比基准数大的数出现
            while left > right and arr[left] <= arr[key]:
                left += 1
            #此时已经找到一个比基准大的数，和一个比基准小的数，将他们互换位置
            arr[left],arr[right] = arr[right],arr[left]

        # 当从两边分别逼近，知道两个位置相等时结束，将左边小的同基准进行交换
        arr[left],arr[key] = arr[key],arr[left]

        #返回目前基准所在位置的索引
        return left

    def quicksort(arr,left,right):
        if left >= right:
            return
        #从基准开始分区
        mid = partition(arr,left,right)
        #递归调用
        quicksort(arr,left,mid-1)
        quicksort(arr,mid+1,right)

    # 主函数
    n = len(list1)
    if n <= 1:
        return list1
    quicksort(list1, 0, n - 1)
    return list1
print("<<< Quick Sort >>>")
x = input("请输入待排序数列：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = quick_sort(arr)
# print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
