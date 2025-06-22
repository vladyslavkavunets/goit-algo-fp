class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def display(self):
        if not self.head:
            print("Список порожній")
            return
        
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def reverse(self):
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def insertion_sort(self):
        if not self.head or not self.head.next:
            return
        
        sorted_head = None
        current = self.head
        
        while current:
            next_node = current.next
            
            if not sorted_head or current.data < sorted_head.data:
                current.next = sorted_head
                sorted_head = current
            else:
                sorted_current = sorted_head
                while sorted_current.next and sorted_current.next.data < current.data:
                    sorted_current = sorted_current.next
                current.next = sorted_current.next
                sorted_current.next = current
            
            current = next_node
        
        self.head = sorted_head
    
    def merge_sort(self):
        if not self.head or not self.head.next:
            return
        
        self.head = self._merge_sort_recursive(self.head)
    
    def _merge_sort_recursive(self, head):
        if not head or not head.next:
            return head
        
        middle = self._find_middle(head)
        next_to_middle = middle.next
        middle.next = None
        
        left = self._merge_sort_recursive(head)
        right = self._merge_sort_recursive(next_to_middle)
        
        return self._merge(left, right)
    
    def _find_middle(self, head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def _merge(self, left, right):
        dummy = Node(0)
        current = dummy
        
        while left and right:
            if left.data <= right.data:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        
        if left:
            current.next = left
        if right:
            current.next = right
        
        return dummy.next


def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    current = dummy
    
    l1 = list1.head
    l2 = list2.head
    
    while l1 and l2:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    if l1:
        current.next = l1
    
    if l2:
        current.next = l2
    
    result = LinkedList()
    result.head = dummy.next
    return result


def demonstrate_reverse():
    print("=== Демонстрація реверсування ===")
    ll = LinkedList()
    for i in [1, 2, 3, 4, 5]:
        ll.append(i)
    
    print("Початковий список:")
    ll.display()
    
    ll.reverse()
    print("Реверсований список:")
    ll.display()
    print()


def demonstrate_sorting():
    print("=== Демонстрація сортування вставками ===")
    ll1 = LinkedList()
    for i in [4, 2, 1, 5, 3]:
        ll1.append(i)
    
    print("Початковий список:")
    ll1.display()
    
    ll1.insertion_sort()
    print("Відсортований список (вставками):")
    ll1.display()
    print()
    
    print("=== Демонстрація сортування злиттям ===")
    ll2 = LinkedList()
    for i in [6, 3, 8, 1, 9, 2]:
        ll2.append(i)
    
    print("Початковий список:")
    ll2.display()
    
    ll2.merge_sort()
    print("Відсортований список (злиттям):")
    ll2.display()
    print()


def demonstrate_merge():
    print("=== Демонстрація об'єднання відсортованих списків ===")
    
    list1 = LinkedList()
    for i in [1, 3, 5, 7]:
        list1.append(i)
    print("Перший відсортований список:")
    list1.display()
    
    list2 = LinkedList()
    for i in [2, 4, 6, 8]:
        list2.append(i)
    print("Другий відсортований список:")
    list2.display()
    
    merged = merge_sorted_lists(list1, list2)
    print("Об'єднаний відсортований список:")
    merged.display()
    print()


def main():
    print("РОБОТА З ОДНОЗВ'ЯЗНИМ СПИСКОМ")
    print("=" * 40)
    
    demonstrate_reverse()
    demonstrate_sorting()
    demonstrate_merge()
    
    print("=== Комплексний приклад ===")
    ll = LinkedList()
    print("Створюємо список: 9, 3, 7, 1, 5")
    for i in [9, 3, 7, 1, 5]:
        ll.append(i)
    ll.display()
    
    print("\nСортуємо список:")
    ll.merge_sort()
    ll.display()
    
    print("\nРеверсуємо відсортований список:")
    ll.reverse()
    ll.display()


if __name__ == "__main__":
    main()