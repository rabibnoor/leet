class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        i = 0
        pos = 0
        while(i<len(nums)):
            if nums[i] >= 0:
                pos = i
                break
            i+=1

        i = 0
        ret = []
        while(i < len(nums)):
            #print("l2", i)
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue
            if nums[i] > 0:
                break
            target = [0]
            if nums[i] < 0:
                target[0] = -nums[i]
            j = i+1
            k = len(nums) - 1
            found = False
            while(j < len(nums) and k  > i and j < k):
                #print("l3")
            
                if nums[j] + nums[k] == target[0]:
                    found = True
                    ret.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                    continue
                    #break
                if nums[j] + nums[k] > target[0]:
                    k -= 1
                else:
                    j+=1
            
           
                

            i+=1

        return ret
                


            
        
                
