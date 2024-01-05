#!/usr/bin/python3
"""Module to create a singly linked list with nodes of class Node
"""


class Node:
    """blueprint for a node

        attributes:
            data (int): Data held by the node
            next_node (Node): Reference to the next node on the list
    """

    def __init__(self, data, next_node=None):
        """Initializes a node with provided data and next node reference

        Args:
            data (int): The data to be held by the node
            next_node (Node, optional): Reference to the next node.
                                    Defaults to None.
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """getter method for retrieving data stored in the node

        Returns:
            data (int): the data stored in the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """setter method for setting node data

        Args:
            value (int): the new value to be set as the node's data

        Raises:
            TypeError: If the value is not an integer

        TODO:
            check if TypeError is raised
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter method for retrieving the reference to the next node

        Returns:
            Node: reference to the next node on the list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter method for setting reference to the next node

        Args:
            value (Node): the next object to be set as next

        Raises:
            TypeError: if the value is not a Node object
        """
        if type(value) != Node:
            raise TypeError("next node must be a node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that represents a singly linked list

        Attributes:
            __head (Node) : the head node of the list. Default is None
    """
    def __init__(self):
        """constructor for the linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """adds elements to the linked list in an increasing order

        Args:
            value (int): the data to be stored by the new element
        """
        new_node = Node(value)
        head_node = self.__head

        # check if the list is empty and make new node the head
        if head_node is None:
            self.__head = new_node
            return

        if head_node.data > value:
            new_node.next_node = head_node
            self.__head = new_node
            return

        while head_node.next_node is not None:
            if head_node.next_node.data > value:
                new_node.next_node = head_node.next_node
                head_node.next_node = new_node
                return

            head_node = head_node.next_node

        head_node.next_node = new_node

    def __str__(self):
        """prints each node element in the list, one per line
        """
        node_list = ""
        current = self.__head
        while current is not None:
            node_list += str(current.data) + "\n"
            current = current.next_node
        return node_list.rstrip("\n")
