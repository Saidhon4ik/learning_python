# #1
# def select_second(L):
#     """Return the second element of the given list. If the list has no second
#     element, return None.
#     """
#     if len(L) > 1:
#         return L[1]
#     else:
#         return None

# print(select_second(L=[[1]]))





#that was from the video, reels from the instagram
# class Solution:
#     def mySqrt(self,x):
#        L,R = 1, x
#        while L <= R:
#               M = (L+R)//2
#               M_squared = M*M

#        if M_squared == x:
#               return M
#        elif M_squared < x:
#               L = M+ 1
#        else: 
#               R = M - 1
#        return R





#https://leetcode.com/problems/two-sum/
# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]





#https://leetcode.com/problems/palindrome-number/
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0 or (x % 10 == 0 and x != 0):
#             return False
#         n = x
#         result = 0
#         while n > 0:
#             result = result * 10 + n % 10
#             n//=10
#         return x == result
# #that was hard gng...





#https://leetcode.com/problems/two-sum/
# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]







# #example of a binary search
# def binary_search(list,target):
#         low = 0
#         high = len(list) - 1

#         while low <= high:
#                 mid = (low+high)//2     
#                 guess = list[mid]

#                 if guess == target:
#                         return mid
#                 elif guess > target:
#                         high = mid - 1
#                 elif guess < target:
#                         low = mid + 1
#         return None

# my_list = [1,3,5,7,9]


# print(binary_search(my_list,1))
# print(binary_search(my_list,-1))
# print(binary_search(my_list,3))







#===============================#
def findSmallest(arr):
        smallest = arr[0]
        smallest_index = 0
        for i in range(1,len(arr)):
                if arr[i] < smallest:
                        smallest = arr[i]
                        smallest_index = i
        return smallest_index
#===============================#
#Selection sort
def selectionSort(arr):
        newArr = []
        for _ in range(0,len(arr)):
                smallest = findSmallest(arr)
                newArr.append(arr.pop(smallest))
        return newArr
#===============================#
print(selectionSort( [1,2,3,4,5,24,75,43,27,745,13]))
#===============================#










#================#
#recursion for countdown from  5 to 0
def countdown(n):
        print(n)
        if n == 0: return 0
        countdown(n-1)
#================#
countdown(5)
#================#






#===================================#
def quicksort(arr):
        if len(arr) <= 1: return arr        
        pivot = arr[0]
        less = []
        greater = []
#===================================#
        for item in arr:
                if item<pivot:
                        less.append(item)
                elif item>pivot:
                        greater.append(item)
        return quicksort(less) + [pivot] + quicksort(greater)
#===================================#
print(quicksort([3, 1, 5, 2, 4]))
#===================================#









#================================================#
#https://leetcode.com/problems/two-sum/ I understood how to do it. lwk cool
nums = [3,4,5,1]
class Solution:
    def twoSum(self, nums, target):
        hashmap = {} #O(1)
        for i,num in enumerate(nums):
                seen = target - num
                if seen in hashmap:
                       return [hashmap[seen], i]
                elif seen not in hashmap:
                       hashmap[num] = i
        return None
#================================================#
print(Solution().twoSum([2,7,9,13,15],9))
#================================================#