#include <stdlib.h>

typedef struct {
    int value;
    int index;
} Pair;

int compare(const void *a, const void *b) {
    Pair *p1 = (Pair *)a;
    Pair *p2 = (Pair *)b;

    if (p1->value < p2->value) return -1;
    if (p1->value > p2->value) return 1;
    return 0;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    Pair *arr = (Pair *)malloc(numsSize * sizeof(Pair));

    for (int i = 0; i < numsSize; i++) {
        arr[i].value = nums[i];
        arr[i].index = i;
    }

    qsort(arr, numsSize, sizeof(Pair), compare);

    int left = 0;
    int right = numsSize - 1;

    while (left < right) {
        int sum = arr[left].value + arr[right].value;

        if (sum == target) {
            int *ans = (int *)malloc(2 * sizeof(int));
            ans[0] = arr[left].index;
            ans[1] = arr[right].index;
            *returnSize = 2;
            free(arr);
            return ans;
        }
        else if (sum < target) {
            left++;
        }
        else {
            right--;
        }
    }

    free(arr);
    return NULL;
}