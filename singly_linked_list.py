class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next

    class LinkedList:
        def __init__(self):
            self.head = None
            self.tail = None

        def add_to_tail(self, value):
            # 1. create the Node from the value
            new_node = Node(value)

            # So, what do we do if tail is none
            # What's the rule we want to set to indicate that the linked list is empty?
            # Would it be better to check the head?
            # Let's check them both: an empty linked list has a empty head and an empty tail
            if self.head is None and self.tail is None:
                # in a one element linked list, what should head and tail be referring to?
                    # have both head and tail referring to the single Node
                self.head = new_node
                # set the new Node to be the tail
                self.tail = new_node
            else:
            # These two steps assume that the tail is already referring to a Node
            # 2. set the old tail's next to refer to the new Node
                self.tail.set_next(new_node)
            # 3. reassign self.tail to refer to the new Node   
                self.tail = new_node

        def remove_head(self):
            # if we have an empty linked list
            if self.head is None and self.tail is None:
                return
            # what if we only have a single elem in the linked list?
            # both head and tail are pointing at the same Node
            if not self.head.get_next():
                head = self.head 
                # delete the linked list's head reference 
                self.head = None
                # also delete the linked list's tail reference 
                self.tail = None 
                return head.get_value()

            val = self.head.get_value()
            # set self.head to the Node after the head
            self.head = self.head.get_next()
            return val

        def remove_tail(self):
            # if we have an empty linked list
            if self.head is None and self.tail is None:
                return

            # if we have a non-empty linked list
            # we have to start at the head and move down the list until we get to the Node right before the tail
            # iterate over our linked list
            current = self.head
            while current.get_next() is not self.tail:
                current = current.get_next()
            # at this point, 'current' is the Node right before the tail
            # set the tail to be None
            val = self.tail.get_value()
            # move self.tail to the Node right before
            self.tail = current
            return val

            

    # ll = Node(1)
    # ll.set_next(Node(2))
    # ll.next.set_next(Node(3))
    # ll.next.next.set_next(Node(4))