class Node: 
    
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList: 
    def __init__(self):
        self.head = None 
        self.n = 0


    def __len__(self):
        return self.n
    

    def insert_head(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1


    def append(self,value):
        current_node = self.head
        if current_node is None:
            self.head = Node(value)
            self.n += 1
            return
        
        while current_node.next !=  None:
            current_node = current_node.next
        current_node.next = Node(value)
        self.n += 1


    def insert_after(self, after, value):

        new_node = Node(value)
        current_node = self.head
        
        while current_node != None:
            if current_node.data == after:
                break
            current_node = current_node.next 
            
        if current_node != None:
            new_node.next = current_node.next
            current_node.next = new_node
        else: 
            return 'Item not found'

    
    def delete_head(self):
        if self.head is None: 
            return "Empty LL"
        self.head = self.head.next
        self.n -= 1


    def clear(self): 
        self.__init__()


    def pop(self):
        current_node = self.head
        if self.head == None:
            return "Empty LL"
        
        if current_node.next is None:
            self.delete_head()
            return
        
        while current_node.next.next != None: 
            current_node = current_node.next

        current_node.next = None
        self.n -= 1


    def remove(self,value):
        if self.head is None:
            return "Empty LL"
        
        if self.head.data  == value:
            self.delete_head()
            self.n -= 1
            return
        
        current_node = self.head
        
        while current_node.next != None:
            if current_node.next.data == value:
                break
            current_node = current_node.next

        if current_node == None: 
            return 'Not Found'
        else: 
            current_node.next = current_node.next.next
            self.n -= 1


    def search(self,value):
        if self.head is None:
            return "Empty LL"
        index = 0
        current_node = self.head
        while current_node != None:
            if current_node.data == value:
                return index
            index += 1
            current_node = current_node.next
        return "Not Found"


    def __getitem__(self,index):
        current_node = self.head
        position = 0

        while current_node != None: 
            if position == index:
                return current_node.data
            current_node = current_node.next
            position += 1
        return 'IndexError'

    """
    Problem: find max value from the linked list and replace it with given value
    traverse over each element of the linked list then store node with bigger value in max_value then 
    replace the data with the given value
    """
    def replace_max(self, value):
        current_node = self.head
        max_value = self.head
        while current_node != None: 
           if current_node.data > max_value.data:
                max_value = current_node
           current_node = current_node.next
        max_value.data = value

    """
    Problem: Sum all the values at the odd index in the linked list
    """
    def sum_odd_nodes(self):
        current_node = self.head
        counter = 0 
        result = 0 

        while current_node != None: 
            if counter % 2 != 0: 
                result += current_node.data

            counter += 1 
            current_node = current_node.next 
        
        return result 

    def __str__(self) -> str:
        result = ""
        curr_node = self.head
        while curr_node !=  None:
            result += f"{curr_node.data}->"
            curr_node = curr_node.next

        return f"{result}None"
    

def main():
    L1 = LinkedList()
    L1.insert_head(1)
    L1.insert_head(2)
    L1.insert_head(3)
    L1.insert_head(4)
    print(L1)
    print(L1.sum_odd_nodes())


if __name__ == "__main__":
    main()