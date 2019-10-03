import inspect

class Queue(object):
    '''
    Queue data structure FIFO - First In First Out
    '''

    def __init__(self, capacity = 10):
        '''
        :param size: max capacity of the queue, default is 10
        '''

        self.queue = []
        self.front = None
        self.rear = None
        self.size = 0
        self.capacity = capacity

    def __str__(self):
        '''

        :return:
        '''

        return ' '.join([str(i) for i in self.queue])

    def get_size(self):
        '''

        :return: current size of the queue
        '''

        return self.size

    def is_empty(self):
        '''

        :return: true if queue is empty, false otherwise
        '''

        return self.size == 0

    def enequeue(self, value):
        '''

        :param value: value to be enqueued
        :return: -1 if queue is full
        '''

        if self.size >= self.capacity:
            return -1

        else:
            self.queue.append(value)

        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size

        self.size += 1


    def dequeue(self):
        '''

        :return: the element removed from the queue, None if queue is empty
        '''

        if self.is_empty():
            return None

        else:
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = 0
            else:
                self.rear = self.size - 1

            return self.queue.pop(0)

    @staticmethod
    def get_code():
        '''

        :return: return source code for current class
        '''
        return inspect.getsource(Queue)


class Deque(object):
    '''
    Deque -> doubly ended queue
    '''

    def __init__(self, capacity = 10):
        '''

        :param capacity: max capacity of the deque
        '''

        self.queue = []
        self.capacity = capacity

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def is_full(self):
        '''
        to check whether deque is full or not
        :return: true if deque is full, false otherwise
        '''
        return len(self.queue) == self.capacity

    def is_empty(self):
        '''
        to check whether deque is empty or not
        :return: true if deque is empty, false otherwise
        '''
        return len(self.queue) == 0

    def insert_right(self, info):
        '''

        :param info: data to be added
        :return: None if deque is full
        '''
        if self.is_full():
            return None
        else:
            self.queue.append(info)

    def insert_left(self, info):
        '''

        :param info: data to be added
        :return: None if deque is full
        '''

        if self.is_full():
            return None
        else:
            self.queue.insert(0, info)

    def remove_left(self):
        '''

        :return: element which is removed, None if deque is empty
        '''

        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None
    def remove_right(self):
        '''

        :return: remove element from right end
        '''

        if self.is_empty():
            return None

        else:
            self.queue.pop()

    @staticmethod
    def get_code():
        '''

        :return: source code for the current class
        '''

        return inspect.getsource(Deque)

# TODO -> add priority queue and circuler queue for concept purpose
















