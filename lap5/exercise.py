import math


def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)

    return stack.pop()


print("Evaluate Postfix:", evaluate_postfix("3 4 + 2 * 7 /"))



class QueueUsingTwoStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item):
        self.stack_in.append(item)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if self.stack_out:
            return self.stack_out.pop()
        else:
            raise IndexError("Dequeue from empty queue")

    def is_empty(self):
        return not self.stack_in and not self.stack_out


q = QueueUsingTwoStacks()
q.enqueue(1)
q.enqueue(2)
print("Queue Using Two Stacks, Dequeue 1:", q.dequeue())  
q.enqueue(3)
print("Queue Using Two Stacks, Dequeue 2:", q.dequeue())  


class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.insert(0, task)

    def process_tasks(self):
        while self.tasks:
            task = self.tasks.pop()
            print(f"Processing task: {task}")

scheduler = TaskScheduler()
scheduler.add_task("Task 1")
scheduler.add_task("Task 2")
scheduler.add_task("Task 3")
print("\nTask Scheduler Processing:")
scheduler.process_tasks()


def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop '('
        else:
            while (stack and stack[-1] != '(' and
                   precedence.get(token, 0) <= precedence.get(stack[-1], 0)):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return ' '.join(output)


print("\nInfix to Postfix:", infix_to_postfix("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"))
