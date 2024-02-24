package org.code.practice.problems;

import java.util.HashMap;
import java.util.Map;

public class EggDrop {
    public static Map<String, Integer> dpMap = new HashMap<String, Integer>();

    private static int tempMin = Integer.MAX_VALUE;
    public static int eggDrop (int k, int n) {
        tempMin = Integer.MAX_VALUE;
        int binaryS = eggDropTest(k, n, 1);
        return binaryS;
    }
    public static int eggDropTest (int k, int n, int l) {
        if (n == 0 || n == 1 || k == 1) {
            return n;
        }
        String mapKey = k+"_"+n;
        if (dpMap.containsKey(mapKey)) {
            return dpMap.get(mapKey);
        }
        int remainderFloors = (l + n) / 2;
        int brokenCase = eggDropTest((k - 1), (remainderFloors - 1), l);
        int notBrokeCase = eggDropTest(k, n - remainderFloors, remainderFloors + 1);
        int result = 1 + Math.max(brokenCase, notBrokeCase);
        tempMin = result = Math.min(result, tempMin);
        dpMap.put(mapKey, result);
        return result;
    }

    private static Integer dp[][];
    public static int superEggDrop(int k, int n) {
        dp=new Integer[k+1][n+1];
        return sol(k,n);
    }
    public static int sol(int k,int n){
        if(k==1 || n==0 || n==1) return n;
        if(dp[k][n]!=null) return dp[k][n];
        int l=1,h=n;
        int ans=Integer.MAX_VALUE;
        while(l<=h){
            int mid=(l+h)/2;
            int k1=sol(k-1,mid-1);
            int k2=sol(k,n-mid);
            int temp=1+Math.max(k1,k2);
            if(k1<k2) l=mid+1;
            else h=mid-1;
            ans=Math.min(temp,ans);
        }
        return dp[k][n]=ans;
    }
    public static void run () {
        int k = 2;
        int n = 3;
        int result = eggDrop(k, n);
//        int result = superEggDrop(k, n);
        System.out.println(result);
    }
}
