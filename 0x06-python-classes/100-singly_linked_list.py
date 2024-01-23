#!/usr/bin/python3
"""define classes for a singly linked list"""


class Node:
    """represent a node in a singly linked list"""

    def __init__(self, data, next_node=None):
        """initialize a new Node"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """return the data private attribute value"""
        return self.__data

    @data.setter
    def data(self, value):
        """set the data private attribute value"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """return the next_node private attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the next_node private attribute value"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a None object")
        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        """initialize a new SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """insert a new Node to the SinglyLinkedList"""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
                new.next_node = tmp.next_node
                tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
