

class BinaryHeap():
    """
    Binary Heap abstract class implementation
    """


    def __init__():
        self.heap = []
        self.count = 0


    def __len__(self):
        return self.count


    def heapify(self, arr):
        raise NotImplementedError('`heapify` function not implemented...')


    def insert(self, val):
        raise NotImplementedError('`insert` function not implemented...')


    def pop(self):
        raise NotImplementedError('`pop` function not implemented...')



class MinHeap(BinaryHeap):
    """
    Min-Heap data structure
    """


    def __init__(arr=None):
        super().__init__()
        if arr != None:
            self.heap = heapify(arr)
            self.count = len(arr)


    def heapify(self, arr):
        res = []
        for x in range(0, arr):
            pass
