#=========================#
#O(1)
#1 Arrays
nums = [1,2,3]
nums.append(4) #push to end
nums.pop()         #pop from end
nums[0]              #lookup
#2 Hashmap/Set
hashmap = {}
hashmap["key"] = 10             #insert
print("key" in hashmap)         #lookup
print(hashmap["key"])            #lookup
hashmap["key"]                      #lookup
#=========================#





#========================#
#O(n)
nums = [1,2,3]
sum(nums)               #sum of array
for num in nums:     #for loop
        print(num)

nums.insert(1,100)      #insert middle
nums.remove(100)     #remove middle
print(100 in nums)      #search


import heapq
heapq.heapify(nums)  #build heap
#========================#








#=========================#
#O(n**2)
#1
nums = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(nums)):
        for j in range(len(nums[i])):
                print(nums[i][j],end = " ")




#2
nums = [1,2,3]
for i in range(len(nums)):
        for j in range(i+1, len(nums)):
                print(nums[i],nums[j])

#=========================#

#insertion sort
#insert in middle  n times -> n**2





#=======================#
#O(n*m)
num1, num2 = [1,2,3],[4,5]
for i in range(len(num1)):
        for j in range(len(num2)):
                print(num1[i],num2[j])


#Traverse rectangle grid
nums = [[1,2,3],[4,5,6]]
for i in range(len(nums)):
        for j in range(len(nums[i])):
                print(nums[i][j])
#=======================#










#============================#
#O(n**3)
#get every triple of elements in array
nums = [1,2,3],[4,1,2],[5,3,1]
for i in range(len(nums)):
        for j in range(i+1,len(nums)):
                for k in range(j+1, len(nums)):
                        print(nums[i],nums[j],nums[k])
#============================#




#=========================#
#O(logn)
#Binary search on BST
...
#binary search
nums = [1,2,3,4,5]
target = 4
def search(nums,target):
        left , right = 0, len(nums) - 1
        while left <= right:
                mid = (left+right)//2
                if target < nums[mid]:
                        right = mid - 1
                elif target > nums[mid]:
                        left = mid + 1
                else:
                        return mid
                        break
print(search(nums,target))


#heap push and pop
import heapq
minHeap = []
heapq.heappush(minHeap,5)
heapq.heappop(minHeap)
#=========================#




#=========================#
#O(nlogn)
#Heap Sort
import heapq
nums = [1,2,3,4,5]
heapq.heapify(nums)              #O(n)
while nums:
        heapq.heappop(nums)   #O(logn)
#MergeSort
#and most built-in sorting functions
#=========================#





#!GARBAGE. NOTHING ELSE TO SAY FR, THAT'S A FKING GARBAGE
# #=========================#
# #O(2**n)
# # Recursion,  tree height n, two branches
# def recursion(i,nums):
#         if i >= len(nums):
#                 return 0
#         branch1 = recursion(i+1,nums[i])
#         branch2 = recursion(i+2,nums[i])
        
#         return max(branch1,branch2)
# print(recursion(0,[2,7,9,3,1]))
# #===========================#






#=========================#
#O(sqrt(n))
import math
n = 12
factors = set()
for i in range(1, int(math.sqrt(n) +1 )):
        if n%i == 0:
                factors.add(i)
                factors.add(n//i)
print(factors)
#=========================#




#=======================#
#O(n!)
#hell nah dude, do that by yourself
#=======================#