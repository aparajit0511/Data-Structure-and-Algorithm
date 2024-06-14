# Time Complexity - O(N log N)
# Space complexity - O(1)

class Solution:
    def heapify(self, arr, n, i):
        largest = i  # Initialize largest as root
        left = 2 * i + 1  # left child index
        right = 2 * i + 2  # right child index

        # If left child is larger than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # If right child is larger than the largest so far
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is not root
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # swap

            # Recursively heapify the affected sub-tree
            self.heapify(arr, n, largest)

    def build_max_heap(self, arr):
        n = len(arr)
        # Build a max heap.
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

    def heap_sort(self, arr):
        n = len(arr)

        # Build a maxheap
        self.build_max_heap(arr)

        # One by one extract elements
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # swap
            self.heapify(arr, i, 0)