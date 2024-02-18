package com.coding.practice.Problems;

public class MaximumProductSubarray {

    private static int maxProduct(int[] nums) {
        int maxValue = Integer.MIN_VALUE;
        for (int num: nums) {
            maxValue = Math.max(num, maxValue);
        }
        int curMinValue = 1, curMaxValue = 1;
        for (int num: nums) {
            int temp = curMaxValue * num;
            curMaxValue = Math.max(temp, Math.max(num * curMinValue, num));
            curMinValue = Math.min(temp, Math.min(num * curMinValue, num));
            maxValue = Math.max(curMaxValue, maxValue);
        }
        return maxValue;
    }
    public static void run () {
        int[] nums = {2, 3, -2, 4};
        int result = maxProduct(nums);
        System.out.println(result);
    }
}
