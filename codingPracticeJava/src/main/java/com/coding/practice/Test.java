package com.coding.practice;

import java.util.Comparator;
import java.util.PriorityQueue;

public class Test {
    public static void run () {
        PriorityQueue<int[]> q = new PriorityQueue<int[]>(new Comparator<int[]>() {
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
        q.add(new int[] {0,4,5});
        q.add(new int[] {1,5,4});
        q.add(new int[] {-1,6,5});
        q.add(new int[] {6,8,5});
        System.out.println(q.poll()[0]);
    }
}
