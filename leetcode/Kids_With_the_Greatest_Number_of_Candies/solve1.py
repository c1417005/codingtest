class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candies = candies
        extra_candies = extraCandies
        result = []

        for num_c in candies:
            if num_c + extra_candies > max(candies):
                result.append(True)
            else:
                result.append(False)

        return result