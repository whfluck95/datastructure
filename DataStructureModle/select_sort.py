"""
选择排序
1.初始化状态：无序区为R[1....N]有序区为空
2.第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。该趟排序从当前无序区中-选出关键字最小的记录 R[k]，将它与无序区的第1个记录R交换，使R[1..i]和R[i+1..n)分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
3.n-1趟结束，数组有序化了。
"""


def select_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst

    for i in range(0, n - 1):
        minIndex = i
        for j in range(i + 1, n):  # 比较一遍，记录索引不交换
            if lst[j] < lst[minIndex]:
                minIndex = j

        if minIndex != i:
            lst[minIndex], lst[i] = lst[i], lst[minIndex]

    return lst


x = input("请输入待排序数列：\n")
y = x.split()
arr = []
for i in y:
    arr.append(int(i))
arr = select_sort(arr)
# print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i, end=' ')
"""
表现最稳定的排序算法之一，因为无论什么数据进去都是O(n2)的时间复杂度，所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧。理论上讲，选择排序可能也是平时排序一般人想到的最多的排序方法了吧。


"""