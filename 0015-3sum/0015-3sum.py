class Solution:
    def threeSum(self, nums):
        res = []  # result
        nums.sort()  # sort the array
        n = len(nums)  # length of array

        # Run i till n-2 because we always need 3 numbers.
        for i in range(n - 2):  # run i till n-2
        
            if nums[i] > 0:  # for early exit, cz if the array is whole positive then we won't get any triplet value, or if array is like [-4, -1, 1, 2, 3] after -1 there is no chance to get any triplet
                break

            # Skip the same number as i to avoid duplicate triplets.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1  # Left pointer starts just after i.
            right = n - 1  # Right pointer starts from the last element.

            # We need left + right to become the opposite of nums[i].
            target = -nums[i]

            # Keep searching until both pointers meet.
            while left < right:

                # Find the sum of left and right elements.
                current_sum = nums[left] + nums[right]

                # If we found the required pair.
                if current_sum == target:

                    # Store the triplet in the result.
                    res.append([nums[i], nums[left], nums[right]])

                    # Move both pointers inward.
                    left += 1
                    right -= 1

                    # Skip duplicate values on the left.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate values on the right.
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                # If the sum is too small, move left to a bigger value.
                elif current_sum < target:
                    left += 1

                # If the sum is too large, move right to a smaller value.
                else:
                    right -= 1

        return res