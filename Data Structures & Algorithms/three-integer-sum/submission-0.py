class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        ret_list = []
        seen = set()  # to avoid duplicate triplets

        for i, num1 in enumerate(nums):
            # Build a value map (count occurrences)
            val_map = {}
            for num2 in nums:
                val_map[num2] = 1 + val_map.get(num2, 0)

            # remove current num1 from availability
            val_map[num1] -= 1
            if val_map[num1] == 0:
                del val_map[num1]

            # Try pairing num1 with every other num3
            for j, num3 in enumerate(nums):
                if j == i:
                    continue  # don't reuse same index

                # temporarily remove num3 from val_map
                if num3 not in val_map:
                    continue
                val_map[num3] -= 1
                if val_map[num3] == 0:
                    del val_map[num3]

                goal = target - num1 - num3
                if goal in val_map:
                    add = sorted([num1, num3, goal])
                    triplet = tuple(add)
                    if triplet not in seen:
                        seen.add(triplet)
                        ret_list.append(add)

                # restore num3 count
                val_map[num3] = 1 + val_map.get(num3, 0)

        return ret_list
