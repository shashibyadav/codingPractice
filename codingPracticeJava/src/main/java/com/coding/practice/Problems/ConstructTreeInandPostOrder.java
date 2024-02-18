package com.coding.practice.Problems;


import com.coding.practice.Utills.TreeNode;


public class ConstructTreeInandPostOrder {

    private static TreeNode buildTreeLogic(int[] inOrder, int[] postOrder) {
        int inStart = 0, postStart = 0;
        int inEnd = inOrder.length - 1;
        int postEnd = postOrder.length - 1;
        return buildTreeHelper(inOrder, inStart, inEnd, postOrder, postStart, postEnd);
    }

    private static TreeNode buildTreeHelper(int[] inOrder, int inStart, int inEnd, int[] postOrder, int postStart, int postEnd) {
        if (inStart > inEnd || postStart > postEnd) {
            return null;
        }
        int rootValue = postOrder[postEnd];
        TreeNode root = new TreeNode(rootValue);

        // Find the index of root in inorder
        int rootIndex = 0;
        for (int i = inStart ; i <= inEnd ; i++) {
            if (inOrder[i] == rootValue) {
                rootIndex = i;
                break;
            }
        }

        root.left = buildTreeHelper(inOrder, inStart, rootIndex - 1, postOrder, postStart, postStart + (rootIndex - inStart) - 1);
        root.right = buildTreeHelper(inOrder, rootIndex + 1, inEnd, postOrder, postStart + (rootIndex - inStart), postEnd - 1);
        return root;
    }
    public static TreeNode buildTree(int[] inorder, int[] postorder) {
        return buildTreeLogic(inorder, postorder);
    }

    public static void run () {
        buildTree(new int[]{9,3,15,20,7}, new int[]{9,15,7,20,3});
    }
}
