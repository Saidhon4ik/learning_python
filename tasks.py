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






# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i,j]