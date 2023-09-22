"""
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.


Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False


Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.


Follow-up: Can you implement the stack using only one queue?
"""
import queue

class MyStack:

    def __init__(self):
        self.data = queue.SimpleQueue()

    def push(self, x: int) -> None:
        self.data.put(x)

    def pop(self) -> int:
        size = self.data.qsize()
        i = 0
        while i < size - 1:
            self.data.put(self.data.get())
            i += 1
        return self.data.get()

    def top(self) -> int:
        size = self.data.qsize()
        i = 0
        while i < size - 1:
            self.data.put(self.data.get())
            i += 1
        res = self.data.get()
        self.data.put(res)
        return res

    def empty(self) -> bool:
        return self.data.empty()


stack = MyStack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.top())

print(stack.pop())

print(stack.pop())

print(stack.empty())

print(stack.pop())

print(stack.empty())