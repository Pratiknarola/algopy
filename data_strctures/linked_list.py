import inspect

class Node(object):
    '''
    Node of linked list
    '''

    def __init__(self, data, next = None):
        '''
        node constructor
        :param data: data in the node
        :param next: link for the next node
        '''

        self.data = data
        self.next = next

    @staticmethod
    def get_code():
        '''

        :return: the code of current class
        '''
        return inspect.getsource(Node)

class SinglyLinkedList(object):

    def __init__(self):
        self.head = None

    def _search(self, node, data):
        '''

        :param node: object of node
        :param data: data to search
        :return: object of node
        '''

        if node is None:
            return None
        if node.data == data:
            return node
        return self._search(node.next, data)

    def get_data(self):
        '''

        :return: python list containing data
        '''

        temp = self.head
        llist = []
        while temp:
            llist.append(temp.data)
            temp = temp.next
        return llist

    def insert_at_start(self, data):
        '''

        :param data: data to be inserted
        :return:
        '''
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, node_data, data):
        '''

        :param node_data: data for node after which data will be inserted
        :param data: data to be inserted
        :return:
        '''
        new_node = Node(data)
        current_node = self._search(self.head, node_data)
        new_node.next = current_node.next
        current_node.next = new_node
        




















