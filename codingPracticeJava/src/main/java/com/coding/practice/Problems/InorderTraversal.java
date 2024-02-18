package com.coding.practice.Problems;

import com.coding.practice.Utills.TreeNode;

import java.util.ArrayList;
import java.util.List;

public class InorderTraversal {
    private void worker (List<Integer> result, TreeNode node) {
        if (node == null) {
            return;
        }
        worker(result, node.left);
        result.add(node.val);
        worker(result, node.right);
    }
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> results = new ArrayList<Integer>();
        worker(results, root);
        return results;
    }
}
