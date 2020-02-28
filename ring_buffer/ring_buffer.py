from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity == self.storage.length:
            # if self.current is the tail
            if self.current == self.storage.tail:
                # then remove from head, add item to head,
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                # and point current to head
                self.current = self.storage.head
            # else insert after current
            else:
                self.current.insert_after(item)
                # change current to currents next
                self.storage.length += 1
                self.current = self.current.next
                # delete what is after the new current
                self.storage.delete(self.current.next)
        # else just add the new item to the tail
        else:
            self.storage.add_to_tail(item)
            # make it the current
            self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head
        # TODO: Your code here
        # if it is only one node
        if self.storage.length == 1:
            # append head.value to the list[]
            list_buffer_contents.append(self.storage.head.value)
        # while next is not pointing to none/while we have not reached the tail
        elif self.storage.length > 1:
            while current.next:
                # append the value of each node to the list
                list_buffer_contents.append(current.value)
                # and move current node ahead one step
                current = current.next
            list_buffer_contents.append(current.value)
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
