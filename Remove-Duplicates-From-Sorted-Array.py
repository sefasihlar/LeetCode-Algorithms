class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # dizi icerisindeki esit olan sayilari kaldir
        if len(nums) == 0:
            return 0
        x = 0
        
        for i in range(len(nums)):
            print(i,x)
            if nums[i] != nums[x]:
                x+=1
                nums[x] = nums[i]
        return x + 1
        

        