package com.coding.practice.Problems;

import com.coding.practice.Utills.TreeNode;

import java.util.*;

public class LevelOrderTraversalTree {
    private void worker(List<List<Integer>> results, TreeNode node, int level) {
        if (node == null) {
            return;
        }
        if (!(level >= 0 && level < results.size())) {
            results.add(new ArrayList<Integer>());
        }
        results.get(level).add(node.val);
        worker(results, node.left, level + 1);
        worker(results, node.right, level + 1);
    }
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> results = new ArrayList<List<Integer>>();
        worker(results, root, 0);
        workerUsingQueue(results, root);
        return results;
    }
    private void workerUsingQueue (List<List<Integer>> results, TreeNode root) {
        if (root == null) {
            return;
        }
        Queue<Integer> levelQ = new LinkedList<Integer>();
        Queue<TreeNode> nodeQ = new LinkedList<TreeNode>();
        nodeQ.add(root);
        levelQ.add(0);
        while (!nodeQ.isEmpty()) {
            TreeNode node = nodeQ.poll();
            int level = levelQ.poll();
            if (!(level >= 0 && level < results.size())) {
                results.add(new ArrayList<Integer>());
            }
            results.get(level).add(node.val);
            if (node.left != null) {
                nodeQ.add(node.left);
                levelQ.add(level + 1);
            }
            if (node.right != null) {
                nodeQ.add(node.right);
                levelQ.add(level + 1);
            }
        }
    }
}
