"""
python 实现单链表模型
思路：
1.节点类：数据区、指针区两个属性
2.链表类：实现链表的 增加、删除、遍历、判断是否为空等功能
"""

class Node:
    """节点类"""
    def __init__(self,elem,next=None):
        self.elem = elem
        self.next = next

class SingleList:
    """创建链表存储空间，创建链表时给元素了，则为非空链表，反之为空链表"""
    def __init__(self,node=None):
        self.head = node

    def is_empty(self):
        """判断链表是否为空"""
        if self.head is None:
            return True
        return False

    def add(self,value):
        """在链表头部添加元素
                1.value节点的指针指向头节点
                2.把value节点设置为头节点
        """
        node = Node(value)
        node.next = self.head
        self.head = node 

    def append(self,value):
        """在链表尾部添加元素
                1.找到尾节点，把尾节点的next指向value节点
                2.把value的节点的next指向None
        """
        node =Node(value)
        if self.is_empty():
            self.head = node
        else:
            current = self.head
            #循环完成后,current指向尾部节点
            while current.next:
                current = current.next
            current.next = node
            node.next = None

    def travel(self):
        """遍历链表
                1.找到头节点，依次往后遍历，打印输出即可（考虑空链表情况）
        """
        if self.is_empty():
            return
        else:
            current = self.head
            while current:
                print(current.elem,end=" ")
                current = current.next

    def length(self):
        """获取链表长度：从头到尾遍历即可"""
        if self.is_empty():
            return 0
        count = 0
        current = self.head
        while current:
            current = current.next
            count += 1
        
        return count

    def get_value(self,position):
        """获取指定下标的元素值"""
        number = self.length()
        if position < 0 or position >(number-1):
            raise Exception('index out of range')
        count = 0
        current = self.head
        while current:
            current = current.next
            count += 1
            if count == position:
                return current.elem

if __name__ == "__main__":
    s = SingleList()
    # 此时为空链表,返回 True
    print(s.is_empty())
    # 链表头部添加2个元素,则结果:111 222
    s.add(222)
    s.add(111)
    # 链表尾部添加2个元素,则结果:111 222 333 555
    s.append(333)
    s.append(555)
    # 遍历链表,则结果: 111 222 333 555 
    s.travel()
    # 获取链表长度,结果: 4
    print(s.length())
    # 获取下表索引为2的,即第三个元素:333
    print(s.get_value(2))