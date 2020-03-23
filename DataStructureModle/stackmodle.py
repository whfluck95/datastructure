"""
python 实现栈
思路：
1.栈的特点：先进后出,一端进行插入和删除操作
2.实现： 可使用列表，列表尾部作为栈顶（进行插入和删除操作），列表头部作为栈底，不做任何操作
"""

class Stack:
    def __init__(self):
        """创建一个空栈"""
        self.stack = []

    def push(self,value):
        """入站操作：相当于在列表尾部进行元素添加"""
        self.stack.append(value)

    def pop(self):
        """出栈操作：相当于在列表尾部弹出一个元素，考虑到空栈的情况"""
        if self.stack == []:
            raise Exception('pop from empty stack')
        else:
            return self.stack.pop

    def is_empty(self):
        """判断栈是否为空"""
        if self.stack == []:
            return True
        else:
            return False

    def  top(self):
        """查看栈顶元素，并非出栈"""
        if self.stack:
            return self.stack[-1]
        print('stack is empty')

    def size(self):
        """返回栈的大小"""
        return len(self.stack)

if __name__ == "__main__":
    s = Stack() 
    print(s.is_empty()) # True
    ## 此时栈中元素为: 111 222 333 ,111在栈底,333在栈顶
    s.push(111)
    s.push(222)
    s.push(333)
    # 从栈顶弹出1个元素,即 333
    print(s.pop)
    # 此时栈不为空,返回 False
    print(s.is_empty())
    # 返回栈顶元素: 222
    print(s.top())
    # 返回栈的大小:2
    print(s.size)
