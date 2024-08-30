import java.util.Arrays;

class Solution {
    int preIndex = 0, postIndex = 0;
    
    public int[][] solution(int[][] nodeinfo) {
        int[][] answer = new int[2][nodeinfo.length];

        Node[] nodes = new Node[nodeinfo.length];
        for (int i = 0; i < nodeinfo.length; i++) {
            nodes[i] = new Node(i + 1, nodeinfo[i][0], nodeinfo[i][1], null, null);
        }
        Arrays.sort(nodes, (a, b) -> { return (a.y == b.y) ? a.x - b.x : b.y - a.y; });

        for (int i = 1; i < nodes.length; i++) makeTree(nodes[0], nodes[i]);

        preorder(nodes[0], answer);
        postorder(nodes[0], answer);

        return answer;
    }

    private class Node {
        int num;
        int x;
        int y;
        Node left;
        Node right;

        public Node(int num, int x, int y, Node left, Node right) {
            this.num = num;
            this.x = x;
            this.y = y;
            this.left = left;
            this.right = right;
        }
    }

    private void makeTree(Node parent, Node chlid) {
        if (parent.x < chlid.x) {
            if (parent.right == null) parent.right = chlid;
            else makeTree(parent.right, chlid);
        } else {
            if (parent.left == null) parent.left = chlid;
            else makeTree(parent.left, chlid);
        }
    }

    private void preorder(Node node, int[][] answer) {
        if (node == null) return;

        answer[0][preIndex++] = node.num;
        preorder(node.left, answer);
        preorder(node.right, answer);
    }

    private void postorder(Node node, int[][] answer) {
        if (node == null) return;

        postorder(node.left, answer);
        postorder(node.right, answer);
        answer[1][postIndex++] = node.num;
    }
} 