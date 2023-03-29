# Python program for implementation of heap Sort
# n is size of heap
def heapify(arr, n, i):
	largest = i # Initialize largest as root
	left = 2 * i + 1	 # left = 2*i + 1
	right = 2 * i + 2	 # right = 2*i + 2

	# See if left child of root exists and is greater than root
	if left < n and arr[largest] < arr[left]:
		largest = left

	# See if right child of root exists and is greater than root
	if right < n and arr[largest] < arr[right]:
		largest = right

	# Change root, if needed
	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] # swap

		# Heapify the root.
		heapify(arr, n, largest)


def heapSort(arr):
	n = len(arr)

	# Build a maxheap.
	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)

	# Extract elements
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] # swap
		heapify(arr, i, 0)

arr = ['S','O','R','T','E','X','A','M','P','L','E']
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
	print("%s"% arr[i],end=" ")
# This code is contributed by Mohit Kumra
