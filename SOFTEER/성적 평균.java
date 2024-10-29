package SOFTEER;

import java.io.*;
import java.util.*;

class 성적평균 {
    private static int[] tree;
    private static int[] score;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nk = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        int n = nk[0], k = nk[1];
        tree = new int[n * 4];
        
        score = new int[n + 1];
        int[] scoreInput = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        for (int i = 1; i <= n; i++) score[i] = scoreInput[i - 1];

        init(1, n, 1);

        for (int i = 0; i < k; i++) {
            int[] ab = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            int a = ab[0], b = ab[1];

            double result = (double) find(1, n, a, b, 1) / (b - a + 1);
            System.out.println(Math.round(result * 100) / 100.0);
        }

        br.close();
    }

    private static int init(int s, int e, int idx) {
        if (s == e) return tree[idx] = score[s];

        int mid = (s + e) / 2;
        return tree[idx] = init(s, mid, idx * 2) + init(mid + 1, e, idx * 2 + 1);
    }

    private static int find(int s, int e, int left, int right, int idx) {
        if (s > right || e < left) return 0;
        if (left <= s && e <= right) return tree[idx];

        int mid = (s + e) / 2;
        return find(s, mid, left, right, idx * 2) + find(mid + 1, e, left, right, idx * 2 + 1);
    }
}
