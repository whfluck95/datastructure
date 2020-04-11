"""
插入排序
特点：平均时间O(N^2) 最坏情况o(n2) 最好情况o(n) 额外空间 o(1)
1.从第一个元素开始，该元素可以认为已经被排序
2.取出下一个元素，在已经排序的元素中从后向前扫描
3.如果该元素（已经排序）大于新元素，讲该元素移到下一位置
4.重复步骤3 知道找到已排序的元素小于或者等于新元素的位置
5.讲新元素插入到该位置中
6.重复步骤2
"""

def insert_sort(list):
    for i in range(1,len(list)):
        print("第{}轮".format(i))

        key = list[i]
        j = i-1
        while j >= 0:
            if list[j]>key:
                list[j+1] = list[j]
                list[j] = key
            j -= 1

        print(list)
    return  list

a = [8,4,5,8,2,7,1]
result = insert_sort(a)