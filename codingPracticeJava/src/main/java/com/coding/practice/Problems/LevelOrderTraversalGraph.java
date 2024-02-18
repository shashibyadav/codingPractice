package com.coding.practice.Problems;

import com.coding.practice.Utills.TreeNode;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class LevelOrderTraversalGraph {
    private void worker(List<List<Integer>> results, Set<Integer> visited, TreeNode node, int level) {
        if (node == null || visited.contains(node.val)) {
            return;
        }
        visited.add(node.val);
        if (!(level >= 0 && level < results.size())) {
            results.add(new ArrayList<Integer>());
        }
        results.get(level).add(node.val);
        worker(results, visited, node.left, level + 1);
        worker(results, visited, node.right, level + 1);
    }
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        Set<Integer> visited = new HashSet<Integer>();
        worker(results, visited, root, 0);
        return results;
    }
}
