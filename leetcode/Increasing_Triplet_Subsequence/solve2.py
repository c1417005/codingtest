class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:

        first = second= float('inf')
        #小 |中｜大

        for n in nums:
            # 小
            if n <= first:
                first = n

            # 中
            elif n <= second:
                second = n

        #より小さいやつが見つかったら更新。
            else:
                return True
            #2つより大きい数字あれば、それが3つ目。

        return False