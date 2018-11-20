

class SortingAlgorithms():
    """
    Collection of basic sorting algorithms without use of special data structures
    """


    def insertionsort(self, arr):
        """ Conducts insertion sort """
        for x in range(1, len(arr)):
            y = x
            temp = arr[y]
            while y > 0 and temp < arr[y-1]:
                arr[y] = arr[y-1]
                y -= 1
            arr[y] = temp
        return arr


    def _merge(self, list1, list2):
        """ Merging function for mergesort """
        res = []
        iterator1 = 0
        iterator2 = 0

        while iterator1 < len(list1) or iterator2 < len(list2):
            if iterator1 >= len(list1):
                res += list2[iterator2:]
                break
            if iterator2 >= len(list2):
                res += list1[iterator1:]
                break

            if list1[iterator1] < list2[iterator2]:
                res.append(list1[iterator1])
                iterator1 += 1
            else:
                res.append(list2[iterator2])
                iterator2 += 1

        return res


    def mergesort(self, arr):
        """ Conducts merge sort """
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.mergesort(arr[:mid])
        right = self.mergesort(arr[mid:])
        return self._merge(left, right)


    def quicksort(self, arr):
        """ Conducts quicksort """
        if len(arr) <= 1:
            return arr

        pivot = arr[-1]
        left = 0
        right = len(arr)-2

        while left <= right:
            while left <= right and arr[left] < pivot:
                left += 1
            while left <= right and arr[right] > pivot:
                right -= 1

            if left <= right:
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
                left += 1
                right -= 1

        arr[-1] = arr[left]
        arr[left] = pivot

        return self.quicksort(arr[:left]) + [pivot] + self.quicksort(arr[left+1:])
