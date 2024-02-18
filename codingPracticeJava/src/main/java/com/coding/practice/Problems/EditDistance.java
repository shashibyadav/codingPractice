package com.coding.practice.Problems;

public class EditDistance {
    private static int[][] dp = null;

    private static int worker (String word1, String word2, int lastIndex1, int lastIndex2) {
        int result;
        if (lastIndex1 == -1) {
            result = lastIndex2 + 1;
        } else if (lastIndex2 == -1) {
            result = lastIndex1 + 1;
        } else if (dp[lastIndex1][lastIndex2] != -1) {
            result = dp[lastIndex1][lastIndex2];
        } else if (word1.charAt(lastIndex1) == word2.charAt(lastIndex2)) {
            result = worker(word1, word2, lastIndex1 - 1, lastIndex2 - 1);
            dp[lastIndex1][lastIndex2] = result;
        } else {
            result = 1 + Math.min(worker(word1, word2, lastIndex1 - 1, lastIndex2), Math.min(worker(word1, word2, lastIndex1, lastIndex2 - 1), worker(word1, word2, lastIndex1 - 1, lastIndex2 - 1)));
            dp[lastIndex1][lastIndex2] = result;
        }
        return result;
    }
    private static int minDistance(String word1, String word2) {
        return worker(word1, word2, word1.length() - 1, word2.length() - 1);
    }
    public static void run () {
        String word1 = "horse";
        String word2 = "ros";
        dp = new int[word1.length()][word2.length()];
        for (int i = 0 ; i < word1.length() ; i++) {
            for (int j = 0 ; j < word2.length() ; j++) {
                dp[i][j] = -1;
            }
        }
        System.out.println(minDistance(word1, word2));
    }
}
