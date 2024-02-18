package com.coding.practice.Problems;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Stack;

public class KthLargest {
    private int k;
    private PriorityQueue<Integer> pQ = new PriorityQueue<Integer>(new Comparator<Integer>() {
        @Override
        public int compare(Integer o1, Integer o2) {
            return 0;
        }
    });
    public KthLargest(int k, int[] nums) {
        this.k = k;
        for (int temp: nums) {
            pQ.add(temp);
        }
    }

    private int getKthElement () {
        Stack<Integer> tempStack = new Stack<Integer>();
        for (int i = 0 ; i < this.k ; i++) {
            tempStack.add(pQ.poll());
        }
        int result = tempStack.peek();
        for (int i = 0 ; i < tempStack.size() ; i++) {
            pQ.add(tempStack.pop());
        }
        return result;
    }

    public int add(int val) {
        pQ.add(val);
        return getKthElement();
    }
    public void run () {
        PriorityQueue<int []> pQ = new PriorityQueue<int []>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] < o2[0]) {
                    return -1;
                } else if (o1[0] > o2[0]) {
                    return 1;
                }
                return 0;
            }
        });
    }
}
