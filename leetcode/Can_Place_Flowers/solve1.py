class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = flowerbed
        planned_n = n
        length_flowerbed = len(flowerbed)

        if n == 0:
            return True

        for i in range(length_flowerbed):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == (length_flowerbed-1) or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                planned_n -= 1

        return planned_n <= 0



        
            
