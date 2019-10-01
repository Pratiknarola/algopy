import  inspect

class Stack(object):
    #constrcutor
    def __init__(self, size = 10):
        '''

        :param size: max capicity of stack
        '''

        self.stack = []
        self.size = size

    def __str__(self):
        return " ".join([str(i) for i in self.stack])

    def push(self, value):
        '''

        :param value: value to be pushed on the stack
        :return: -1 if overflow occurs
        '''
        if(len(self.stack)) >= self.size:
            return -1

        else:
            self.stack.append(value)

    def pop(self):
        '''

        pops the top most element of the stack

        :return: element removed ,  None if underflow occurs
        '''

        if len(self.stack) <= 0:
            return None

        else:
            return self.stack.pop()

    def peek(self):
        '''

        to see the top most element without removing the element
        :return: the topmost element without removing it
        '''

        if len(self.stack) <= 0:
            return None

        else:
            return self.stack[-1]

    def is_empty(self):
        '''
        to check whether stack is empty or not
        :return: true if stack if empty false otherwise
        '''

        return self.current_size() == 0

    def current_size(self):
        '''
        returns the number of element in stack
        :return:
        '''

        return len(self.stack)

    @staticmethod
    def get_code():
        '''

        :return: code for the class
        '''

        return inspect.getsource(Stack)


'''
 TO DO :
    add files for infix prefix postfix application files in application folder
        
   '''

















