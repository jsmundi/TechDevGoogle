'''

Consider the leftmost and righmost appearances of some value in an array. 
We'll say that the "span" is the number of elements between the two inclusive. 
A single value has a span of 1. Returns the largest span found in the given array. 
(Efficiency is not a priority) 

maxSpan([1, 2, 1, 1, 3]) → 4
maxSpan([1, 4, 2, 1, 4, 1, 4]) → 6
maxSpan([1, 4, 2, 1, 4, 4, 4]) → 6
'''

def maxSpan(nums):

	lenNum = len(nums)

	i = 0
	j = 0
	span = 0
	highestSpan = 0
	

	while i < lenNum:
		j = i + 1

		while j < lenNum:

			if(nums[i] == nums[j]):
				span = (j-i+1)

				if(span > highestSpan):
					highestSpan = span

			j = j + 1

		i = i + 1

	print(highestSpan)
	return highestSpan 



nums = [11, 4, 2, 1, 4, 4, 4]
maxSpan(nums)
