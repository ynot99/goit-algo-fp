class Node:
    next: "Node | None"
    data: int

    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head: Node | None = None

    def insert_at_beginning(self, data: int):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data: int):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data: int):
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None or prev is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        print("[", end="")
        while current:
            print(current.data, end=", " if current.next else "")
            current = current.next
        print("]")

    def reverse(self):
        prev = None
        current = self.head
        # Until we hit the end of the list
        while current is not None:
            # Remember the next node
            next_node = current.next
            # Reverse the link for current node
            current.next = prev
            # Prepare for next iteration by moving prev and current to the next node
            prev = current
            current = next_node

        # Update head to the new first element
        self.head = prev

    def __split(self, head: Node) -> Node | None:
        fast = head
        slow = head

        # Move fast pointer two steps and slow pointer
        # one step until fast reaches the end
        # We also check that slow is not None to avoid type checker issues
        while fast and fast.next and slow:
            fast = fast.next.next
            if fast:
                slow = slow.next

        # Also check if slow is None to avoid type checker issues
        if slow is None:
            return None

        # Split the list into two halves
        second = slow.next
        slow.next = None
        return second

    def __merge(self, first: Node | None, second: Node | None) -> Node | None:
        # If either list is empty, return the other list
        if first is None:
            return second
        if second is None:
            return first

        # Pick the smaller value between first and second nodes
        if first.data < second.data:
            first.next = self.__merge(first.next, second)
            return first
        else:
            second.next = self.__merge(first, second.next)
            return second

    def __merge_sort_recursive(self, head: Node | None) -> Node | None:
        # Base case: if the list is empty or has only one node,
        # it's already sorted
        if not head or not head.next:
            return head

        # Split the list into two halves
        second = self.__split(head)

        # Recursively sort each half
        head = self.__merge_sort_recursive(head)
        second = self.__merge_sort_recursive(second)
        # Merge the two sorted halves
        return self.__merge(head, second)

    def merge_sort(self):
        self.head = self.__merge_sort_recursive(self.head)

    def merge(self, other: "LinkedList") -> "LinkedList":
        merged_list = LinkedList()
        merged_list.head = self.__merge(self.head, other.head)
        return merged_list


if __name__ == "__main__":
    # Prepare two linked lists
    llist = LinkedList()
    llist.insert_at_beginning(15)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(25)
    llist.insert_at_end(20)
    llist.insert_at_end(5)
    llist.insert_at_beginning(45)
    llist.insert_at_beginning(35)
    llist.insert_at_end(30)
    llist.insert_at_beginning(40)

    llist2 = LinkedList()
    llist2.insert_at_end(12)
    llist2.insert_at_end(18)
    llist2.insert_at_end(22)
    llist2.insert_at_beginning(8)

    # Print both lists
    print("First Linked List:")
    llist.print_list()
    print("\nSecond Linked List:")
    llist2.print_list()

    # Sort both lists, merge them, print the merged list, and then reverse it and print again
    llist.merge_sort()
    llist2.merge_sort()

    new_list = llist.merge(llist2)

    print("\nMerged and Sorted Linked List:")
    new_list.print_list()
    new_list.reverse()

    print("\nThe same list but reversed:")
    new_list.print_list()
