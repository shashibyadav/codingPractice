package org.code.practice.problems;

public class MathworksTest {

    public static void run () {
        int[] arr = {4,1,2,3,1};
        int n = arr.length;
        int mod = 1000000007;

        // Calculate longest increasing subsequences (lis)
        int[] lis = new int[n];
        lis[0] = 1;
        for (int i = 1; i < n; i++) {
            lis[i] = 1;
            for (int j = 0; j < i; j++) {
                if (arr[j] < arr[i]) {
                    lis[i] = Math.max(lis[i], lis[j] + 1);
                }
            }
        }

        // Reverse the array for calculating longest decreasing subsequences (lds)
        int[] reversedArr = new int[n];
        for (int i = 0; i < n; i++) {
            reversedArr[i] = arr[n - 1 - i];
        }

        // Calculate longest decreasing subsequences (lds) in the reversed array
        int[] lds = new int[n];
        lds[0] = 1;
        for (int i = 1; i < n; i++) {
            lds[i] = 1;
            for (int j = 0; j < i; j++) {
                if (reversedArr[j] < reversedArr[i]) {
                    lds[i] = Math.max(lds[i], lds[j] + 1);
                }
            }
        }

        // Reverse lds back to match the original order
        for (int i = 0; i < n / 2; i++) {
            int temp = lds[i];
            lds[i] = lds[n - 1 - i];
            lds[n - 1 - i] = temp;
        }

        // Count bitonic subsequences
        long result = 0;
        for (int i = 0; i < n; i++) {
            long count = 0;
            for (int j = 0; j < i; j++) {
                if (arr[j] < arr[i] && (i + 1) < lds.length) {
                    count = (count + (lis[j] * lds[i + 1]) % mod) % mod;
                } else if (arr[j] > arr[i] && (i + 1) < lis.length) {
                    count = (count + (lds[j] * lis[i + 1]) % mod) % mod;
                }
            }
            result = (result + count) % mod;
        }

//        return (int) result;
        System.out.println(result);
    }

}
