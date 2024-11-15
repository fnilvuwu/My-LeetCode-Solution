class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def get_key(val):
        
            for key, value in myDict.items():
                if val == value:
                    return key
        
            return "key doesn't exist"

        myDict = {}

        for i in range(len(nums)):
            if nums[i] in myDict.values():
                return [i, get_key(nums[i])]
            else:
                myDict[i] = target - nums[i] 
