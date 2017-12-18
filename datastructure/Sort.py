class QuickSort:
	def sort(self, a):
		self.__sort(a, 0, len(a) - 1)

	def __sort(self, a, low, high):
		if low >= high:
			return

		pivot = self.__partition(a, low, high)
		self.__sort(a, low, pivot - 1)
		self.__sort(a, pivot + 1, high)

	def __partition(self, a, low, high):
		mid = (high + low) // 2
		p = a[mid];
		i = low
		j = high

		tmp = a[low]
		a[low] = a[mid]
		a[mid] = tmp
		while (i < j):
			while (i <= high and a[i] <= p):
				i = i + 1
			while (j >= low and a[j] > p):
				j = j - 1
			if i > j:
				break

			temp = a[i]
			a[i] = a[j]
			a[j] = temp

			i = i + 1
			j = j - 1

		tmp = a[low]
		a[low] = a[j]
		a[j] = tmp	
		return j

#####
sort = QuickSort()
# a = [15,65,12,48,78,100,99]
# sort.sort(a)
# print(a)

f = open('BST/test.txt', 'r')
N = f.readline()
items = list(map(int, f.readline().split()))
sort.sort(items)
print(items)