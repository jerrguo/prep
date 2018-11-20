import warnings


class BinarySearch():
    """
    Basic binary search algorithm
    """

    def _binary_search(self, array, left, right, target):
        """
        Recursive function to conduct binary search
        """
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
        Returns the index of a target in a sorted list or -1 if it doesn't exist
        """
        if array != array.sort():
            message = 'The given array for binary search is not sorted... ' + \
                      'Results will be based on the sorted array.'
            warnings.warn(message, Warning, stacklevel=2)

        return self._binary_search(array, 0, len(array), target)
