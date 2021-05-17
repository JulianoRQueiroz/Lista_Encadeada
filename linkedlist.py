from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0 
        
    def append(self, element):
        if self.head:
            # inserção quando a lista já possui elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(element)
        else:
            #primeira inserção
            self.head = Node(element)
        
        self._size = self._size + 1
    
    def __len__(self):
        """ Retorna o tamanho da lista"""
        return self._size
    
    def _getnode(self, index):
        pointer = self.head
        
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError('list index out or range')
        return pointer
    
    def __getitem__(self, index):
        pointer = self._getnode(index)
        
        if pointer:
            return pointer.data
        else:
            raise IndexError('list index out or range')
    
    def set(self, index, element):
        pass
        
    def __setitem__(self, index, element):
        pointer = self._getnode(index)
        
        if pointer:
            pointer.data = element
        else:
            raise IndexError('list index out or range')
    
    def index(self, element):
        """ Retorna o indice do elemento na lista"""
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == element:
                return i 
            pointer = pointer.next
            i = i + 1
        raise ValueError(f"{element} is not list")
    
    def insert(self, index, element):
        node = Node(element)
        if index == 0:
            node.next = self.head
            self.head = node 
        else: 
            pointer = self._getnode(index - 1)   
            node.next = pointer.next   
            pointer.next = node 
        
        self._size = self._size + 1
        
    def remove(self, element):
        if self.head == None:
            raise ValueError(f"{element} is not list")
        elif self.head.data == element:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == element:
                    # remove
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = ancestor
                pointer = pointer.next
            self._size = self._size - 1
            return True
        raise ValueError(f"{element} is not list")
    
    def __repr__(self) -> str:
        r = ""
        pointer = self.head
        while(pointer):
            r = r + str(pointer.data) + ' -> '
            pointer = pointer.next
        return r
        
    def __str__(self) -> str:
        return self.__repr__()
        