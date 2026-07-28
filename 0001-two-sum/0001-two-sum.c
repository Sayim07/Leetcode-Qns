#include <stdlib.h>

int* twoSum(int* numbers, int numbersSize, int target, int* returnSize) {
    int left = 0;
    int right = numbersSize - 1;

    *returnSize = 2;
    int *ans = (int *)malloc(2 * sizeof(int));

    while (left < right) {
        int sum = numbers[left] + numbers[right];

        if (sum == target) {
            ans[0] = left + 1;   // Convert to 1-based indexing
            ans[1] = right + 1;
            return ans;
        }
        else if (sum < target) {
            left++;
        }
        else {
            right--;
        }
    }

    return NULL;
}
