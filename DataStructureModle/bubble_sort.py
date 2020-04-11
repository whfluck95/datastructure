"""
冒泡排序
1.比较相邻的元素，如果第一个比第二个大，就交换他们两个
2.对每一对相邻元素同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数
3.针对所有的元素重复以上的步骤，除了最后一个。
4.重复步骤1-3 直到完成排序
o(n2) o(n2) o(n) O(1) 稳定
"""

def bubble_sort(list1):
    n = len(list1)
    if n <= 1:
        return list1
    for i in range(0,n):
        for j in range(0,n-i-1):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]

    return list1

list1 = [ 8,1,3,9,4,7,6,2]


print(bubble_sort(list1))