# from dll_stack import Stack
# from dll_queue import Queue
# import sys
# sys.path.append('../queue_and_stack')


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)

    """Removes the input node from its current spot in the
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        if node is self.head:
            self.remove_from_head()
        else:
            node.delete()
            self.length -= 1

        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        self.length -= 1
        if not self.head and not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        current_node = self.head
        while current_node:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next
        return max_value


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        return self.size


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        return self.size


class NodeTree:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        # self.tree = NodeTree(value)

    # Insert the given value into the tree
    def insert(self, value):
        # if self.tree.value is None:
        #     self.tree.value = value
        #     return
        # else:
        current_node = self
        while current_node:
            # check if our current node value is greater than the value to insert
            if current_node.value > value:
                # go left
                if current_node.left:
                    # if there's a left child set that to the tree(current_node) and repeat
                    current_node = current_node.left
                else:
                    # else our node leaf is home
                    current_node.left = BinarySearchTree(value)
                    return
            else:
                # go right
                if current_node.right:
                  # if there's a right child set that to the tree(current_node) and repeat
                    current_node = current_node.right
                else:
                    # else our node leaf is home
                    current_node.right = BinarySearchTree(value)
                    return
        return

    def contains(self, target):

        current_node = self

        while current_node:
            if current_node.value == target:
                return True

            if current_node.value > target:
                if current_node.left:
                    current_node = current_node.left
                    return
            else:
                if current_node.right:
                    current_node = current_node.right
                    return

        return current_node

    # def get_max(self):
    #     current_node = self
    #     def get_max_helper(current_node):
    #         if current_node.right is None:
    #             return current_node.value
    #         return get_max_helper(current_node.right)
    #     return get_max_helper(current_node)

    def get_max(self):
        current_node = self
        while current_node.right:
            current_node = current_node.right

        return current_node.value

    def for_each(self, cb):
        current_node = self
        cb(current_node.value)

        def for_each_helper(current_node, cb):
            if current_node is None:
                return
            else:
                cb(current_node.value)
                for_each_helper(current_node.right, cb)
                for_each_helper(current_node.left, cb)
                return
        return for_each_helper(current_node, cb)

    # DAY 2 Project - ----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        if not node:
            return
        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):
        if not node:
            return
        queue = Queue()
        current_node = self
        queue.enqueue(current_node)

        while queue.len():
            current_node = queue.dequeue()
            print(current_node.value)
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)

        # Print the value of every node, starting with the given node,
        # in an iterative depth first traversal

    def dft_print(self, node):
        if not node:
            return
        stack = Stack()
        current_node = self
        stack.push(current_node)

        while stack.len():
            current_node = stack.pop()
            print(current_node.value)
            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)

        # STRETCH Goals - ------------------------
        # Note: Research may be required

        # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        if not node:
            return

        print(node.value)
        self.pre_order_dft(node.left)
        self.pre_order_dft(node.right)

        # Print Post-order recursive DFT

    def post_order_dft(self, node):
        if not node:
            return
        self.post_order_dft(node.left)
        self.post_order_dft(node.right)
        print(node.value)
