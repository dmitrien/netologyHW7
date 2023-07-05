from PEP8 import MailWork

class Stack:

    def __init__(self, stack: str = ''):
        self.stack = list(stack)

    def is_empty(self):
        return bool(self.stack)

    def push(self, item: str):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)


def balance(stack: Stack, start ='[{(', end =']})'):
    if stack.is_empty():
        if stack.size() % 2 != 0:
            return 'Несбалансированно'
        if stack.peek() in end:
            return 'Несбалансированно'
        while stack.is_empty():
            v = stack.pop()

            if v in start:
                i = v
            elif v in end:
                if i not in end and start.index(i) != end.index(v) :
                    return 'Несбалансированно'
                i = v
        return 'Cбалансированно'



if __name__ == '__main__':
    mailWork = MailWork()
    mailWork.sendMessage(['vasya@email.com', 'petya@email.com'], 'Subject', 'Message')
    mailWork.recieve()


    # print(balance(Stack('{{[]()}}')))
