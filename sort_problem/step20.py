nums = [1, 5, 9, 7, 5, 3, 2, 5, 8, 4]
S = [0]

for i in range(len(nums)):
    S.append(S[i] + nums[i])

results = []
for j in range(len(nums) - 3):
    results.append(S[i + 3] - S[i])

print(max(*results))
