class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        nums = nums
        nums_length = len(nums)
        n = nums[0]
        triplet = [nums[n]]*3
        triplet[0] = n
        is_triplet = False

        triplet_id = 0
        while not is_triplet:
            for i in range(1,nums_length):

                if triplet_id == 1 and i == nums_length - 2:
                    return False
                
                if nums[i] > n:
                    n = nums[i]
                    triplet[triplet_id] = n
                    triplet_id += 1

                if i == nums_length-1 and triplet_id != 2:
                    triplet_id = 0
                    triplet = [nums[i]]*3
                    continue

                if triplet_id == 2:
                    triplet_id = 0
                    x = nums[triplet[0]]
                    y = nums[triplet[1]]
                    z = nums[triplet[2]]

                    if x < y and y < z:
                        return True
                    triplet = [nums[i]]*3

            
