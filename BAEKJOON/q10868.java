import java.io.*;

public class q10868 {
    static int[] ary, segmentTree;
    public static void main(String [] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] nm = br.readLine().split(" ");
        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);

        ary = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            ary[i] = Integer.parseInt(br.readLine());
        }

        segmentTree = new int[n * 4];
        init(1, n, 1);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            String[] ab = br.readLine().split(" ");
            int a = Integer.parseInt(ab[0]);
            int b = Integer.parseInt(ab[1]);

            sb.append((find(1, n, 1, a, b)) + "\n");
        }
        System.out.print(sb.toString());
        br.close();
    }

    private static int init(int start, int end, int node) {
        if (start == end) return segmentTree[node] = ary[start];

        int mid = (start + end) / 2;
        return segmentTree[node] = Math.min(init(start, mid, node * 2), init(mid + 1, end, node * 2 + 1));
    }

    private static int find(int start, int end, int node, int left, int right) {
        // 범위를 벗어난 경우
        if (start > right || end < left) return Integer.MAX_VALUE;

        // 범위 안에 있는 경우
        if (start >= left && end <= right) return segmentTree[node];

        int mid = (start + end) / 2;
        return Math.min(find(start, mid, node * 2, left, right), find(mid + 1, end, node * 2 + 1, left, right));
    }
}
