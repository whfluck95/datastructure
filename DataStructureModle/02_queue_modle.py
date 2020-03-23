""""
python 实现队列
思路：
1.队列特点：先进先出，队尾入队，队头出队
2.可以用列表实现，列表尾部作为队列尾部进行入队操作，列表头部作为队头进行出队操作
"""

class   Queue:
    def __init__(self):
        """创建一个空队列"""
        self.queue = []

    def enqueue(self,value):
        """入队列：从列表尾部添加元素"""
        self.queue.append(value)

    def dequeue(self):
        """出队列：从列表头部弹出元素，考虑队列为空的特殊情况"""
        if self.queue == []:
            raise Exception('dequeue from empty queue')
        return self.queue.pop(0)

    def is_empty(self):
        """判对队列是否为空"""
        if self.queue == []:
            return True
        return False

    def top(self):
        """查看队头元素，考虑为空队列的情况"""
        if self.queue:
            return self.queue[0]
        else:
            raise Exception('queue is empty')

    def travel(self):
        """遍历整个队列，从队列头到队列尾部输出"""
        for i in self.queue:
            print(i,end=" ")
        print()

if __name__ == "__main__":
    q = Queue()
    # 此时为空队列,返回 True
    print(q.is_empty())
    # 此时队列中元素为 : 111 222 333
    q.enqueue(111)
    q.enqueue(222)
    q.enqueue(333)
    # 队头出队列,结果为:111
    print(q.dequeue())
    # 此时队列不为空,返回:False
    print(q.is_empty())
    # 获取队头元素,结果为:222
    print(q.top())
    # 队头到队尾元素:222 333
    q.travel()