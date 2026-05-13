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





# #https://leetcode.com/problems/two-sum/ not done yet as i have to understand it more properly
# nums = [3,4,5,1]
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         h = {}
#         for i in range(len(nums)):
#             h[nums[i]] = i
#         for i in range(len(nums)):
#             y = target - nums[i]
        
#         if y in h and h[y]  != i:
#             return [i,h[y]]



#example of a binary search
def binary_search(list,target):
        low = 0
        high = len(list) - 1

        while low <= high:
                mid = (low+high)//2     
                guess = list[mid]

                if guess == target:
                        return mid
                elif guess > target:
                        high = mid - 1
                elif guess < target:
                        low = mid + 1
        return None

my_list = [1,3,5,7,9]


print(binary_search(my_list,1))
print(binary_search(my_list,-1))
print(binary_search(my_list,3))