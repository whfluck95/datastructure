"""
python实现单项循环链表
思路:
1. 节点类: 数据区 指针区 两个属性
2. 链表类: 实现链表的 增加、删除、遍历、判断是否为空等功能
3. 单向循环链表特点: 尾节点指向头节点
"""


class Node:
    """节点"""
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SingleList:
    def __init__(self, node=None):
        """创建空链表,创建链表时给元素了,则为非空链表,反之为空链表"""
        self.head = node
        if node:
            node.next = node

    def is_empty(self):
        """判断链表是否为空"""
        if self.head is None:
            return True
        return False

    def add(self, val):
        """链表头部添加1个节点
           1. value节点的指针指向原来的头节点
           2. 把value节点设置为新的头节点
           3. 把尾节点指向value节点
        """
        node = Node(val)
        if self.is_empty():
            self.head = node
            node.next = node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next

            node.next = self.head
            self.head = node
            current.next = self.head

    def append(self, val):
        """在链表的尾部添加1个元素
           1.找到尾节点,把尾节点的next指向 value 节点
           2.把value节点的next指向 头节点
        """
        node = Node(val)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            current = self.head
            # 循环完成后,current指向尾节点
            while current.next != self.head:
                current = current.next

            current.next = node
            node.next = self.head

    def travel(self):
        """遍历链表:
           1.找到头节点,依次往后遍历,打印输出即可（考虑空链表）
        """
        if self.is_empty():
            return
        else:
            current = self.head
            while current.next != self.head:
                print(current.value, end=" ")
                current = current.next
            # 循环结束,current指向尾节点但是并没有打印
            print(current.value)

    def length(self):
        """获取链表长度: 从头到为遍历"""
        if self.is_empty():
            return 0
        else:
            count = 1
            current = self.head
            while current.next != self.head:
                current = current.next
                count += 1

        return count

    def get_value(self, index):
        """获取指定下标的元素值,index从0开始"""
        pass

    def remove(self, val):
        """移除某个节点"""
        pass


if __name__ == '__main__':
    s = SingleList()
    # 链表头部添加2个元素: 111 222
    s.add(222)
    s.add(111)
    # # 链表尾部添加2个元素: 111 222 333 555
    s.append(333)
    s.append(555)
    # 结果: False
    print(s.is_empty())
    # 遍历: 111 222  333  555
    s.travel()
    # 长度: 4
    print(s.length())