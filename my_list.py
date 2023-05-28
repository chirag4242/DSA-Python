import ctypes 

class MyList: 
    def __init__(self):
        # show the max number of items can be in the list
        self.size = 1 
        self.n = 0 
        # create ctype array with list = self.size items
        self.A = self.__make_array(self.size)


    def __make_array(self,capacity):
        #ctype array(static, referential array) with size capacity
        return (capacity*ctypes.py_object)()


    def clear(self):
        self.n = 0
        self.size = 0


    def pop(self):
        if self.n == 0: 
            print("No more elements")
            return 'Empty list'
        print(self.A[self.n-1])
        self.n = self.n - 1 


    def __getitem__(self,index):
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'Index out of range'
         

    def __resize(self, new_capacity):
        # create new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        # copy the content of A to B
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B 
    

    def __str__(self):
        # display list [1,2,3]
        result = ""
        for i in range(self.n):
            state = "," if self.n != i + 1 else ""
            result += str(self.A[i]) + state
        return "[" + result + "]"
    

    def insert(self,pos,item):
        if self.n == self.size:
            self.__resize(self.size*2)

        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]
        self.A[pos] = item
        self.n += 1     


    def append(self,item):
        if self.n == self.size: 
            # resize array
            self.__resize(self.size*2)
            
        # append item
        self.A[self.n] = item
        self.n += 1


    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item: 
                return i 
        return 'ValueError: not in list'


    def __len__(self):
        return self.n
    

    def __delitem__(self, pos):
        if 0 <= pos  < self.n:
            for i in range(pos,self.n-1):
                self.A[i] = self.A[i+1]
            self.n -= 1
        

    def remove(self, item):
        pos = self.find(item)
        if type(pos) == int:
            self.__delitem__(pos)
        else: 
            return "ValueError - not in the list"
                    
def main():
    L = MyList()
    L.append('hello')
    L.append(3.4)
    print(L)
    L.insert(1, 'Destroy')
    print(L)


if __name__ ==  "__main__":
    main()
