
class BinarySearch():
    """
    Basic binary search algorithm
    """

    def _binary_search(self, array, left, right, target):
        mid = (right - left) // 2 + left
        if left > right:
            return -1
        if array[mid] == target:
            return mid

        if array[mid] < target:
            return self._binary_search(array, mid + 1, right, target)
        else:
            return self._binary_search(array, left, mid - 1, target)


    def binary_search(self, array, target):
        """
        Returns the location of a target in a list or -1 if it doesn't exist
        """
        array.sort()
        return self._binary_search(array, 0, len(array), target)
