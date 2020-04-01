"""
【1】题目描述
用两个栈来实现一个队列,完成队列的 Push 和 Pop 操作。队列中的元素为 int 类型
【2】试题解析
1、队列特点:先进先出(时刻铭记保证先进先出)
2、栈 A 用来做入队列,栈 B 用来做出队列,当栈 B 为空时,栈 A 全部出栈到栈 B,栈B 再出栈(即出队
列)
3、精细讲解
stack_a: 入队列(队尾)
stack_b: 出队列(队头)
stack_a队尾: [1,2,3]
stack_b队头: []
stack_b.append(stack_a.pop()) # [3,2,1]
stack_b.pop() # 1
"""

class Solution:
    def __init__(self):
        #创建两个栈空间
        self.stack_a = []
        self.stack_a = []

    def push(self,val):
        """入队列：栈a用来如队列"""
        self.stack_a.append(val)

    def pop(self):
        """出队列：栈b用来出队列"""
        if self.stack_b:
            return self.stack_b.pop()
        else:
            while self.stack_a:
                self.stack_b.append(self.stack_a.pop())
            return self.stack_b.pop()


if __name__ == "__main__":
    q = Solution()
    q.stack_a = [1,2,3]
    q.stack_b = []
    print(q.pop())




