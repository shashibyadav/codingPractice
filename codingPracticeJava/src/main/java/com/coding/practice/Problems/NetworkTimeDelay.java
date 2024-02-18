package com.coding.practice.Problems;

import java.util.*;

class Tuple  implements Comparable<Tuple>{
    public int weight;
    public int node;
    public Tuple (int weight, int destination) {
        this.weight = weight;
        this.node = destination;
    }
    @Override
    public int compareTo (Tuple temp) {
        return Integer.compare(this.weight, temp.weight);
    }

    @Override
    public int hashCode () {
        return this.node;
    }

    @Override
    public boolean equals (Object temp) {
        Tuple second = null;
        try {
            second = (Tuple) temp;
        } catch (Exception e) {
            return false;
        }
        return this.node == second.node;
    }

    @Override
    public String toString () {
        return "Weight: " + this.weight + ", Node: " + this.node;
    }
}

public class NetworkTimeDelay {
    private static int networkDelayTime(int[][] times, int n, int k) {
        int startingNode = k - 1;
        // initializing graph
        List<List<Integer>> adjM = new LinkedList<List<Integer>>();
        int[][] graph = new int[n][n];
        for (int i = 0 ; i < n ; i++) {
            adjM.add(new LinkedList<Integer>());
            for (int j = 0 ; j < n ; j++) {
                graph[i][j] = Integer.MAX_VALUE;
            }
        }

        // setting time
        for (int[] path: times) {
            int s = path[0] - 1;
            int d = path[1] - 1;
            int w = path[2];
            graph[s][d] = w;
            adjM.get(s).add(d);
        }
        Set<Integer> visitedNodes = new HashSet<Integer>();
        PriorityQueue<Tuple> pQueue = new PriorityQueue<Tuple>();

        Map<Integer, Integer> table = new HashMap<Integer, Integer>();
        for (int i = 0 ; i < n ; i++)  {
            table.put(i, Integer.MAX_VALUE);
        }

        pQueue.add(new Tuple(0, startingNode));
        table.put(startingNode, 0);
        while ((!pQueue.isEmpty())) {
            Tuple curr = pQueue.poll();
            int curNode = curr.node;
            int currW = curr.weight;
            if (currW > table.get(curNode) || visitedNodes.contains(curNode)) {
                continue;
            }
            visitedNodes.add(curNode);
            int currPathLen = table.get(curNode);
            for (int neighbour: adjM.get(curNode)) {
                int newWeight = graph[curNode][neighbour];
                int newPath = currPathLen + newWeight;
                if (newPath < table.get(neighbour)) {
                    table.put(neighbour, newPath);
                    pQueue.add(new Tuple(newPath, neighbour));
                }
            }
        }

        int maxTime = 0;
        for (int key : table.keySet()) {
            if (table.get(key) == Integer.MAX_VALUE) {
                return -1;
            }
            maxTime = Math.max(table.get(key), maxTime);
        }
        return maxTime;
    }
    public static void run () {
        int[][] input = new int[][]{
                {2,1,1},
                {2,3,1},
                {3,4,1}
        };
        int result = networkDelayTime(input , 4, 2);
        System.out.println(result);
    }
}
