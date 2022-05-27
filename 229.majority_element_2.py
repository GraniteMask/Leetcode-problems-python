# Optimized and O(1) solution using Boyer-Moore's algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        
        if not nums: return []

        count1, count2, res1, res2 = 0,0,0, 1
        
        for n in nums:
            
            if n == res1:
                count1 += 1
            elif n == res2:
                count2 += 1
                
            elif count1 == 0:
                res1 = n
                count1 += 1
            elif count2 == 0:
                res2 = n
                count2 += 1
                
            else:
                count1 = count1 - 1
                count2 = count2 - 1
                
        print(res1,res2)
        
        return [res for res in (res1,res2) if nums.count(res) > len(nums)//3]
    
    