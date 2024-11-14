package SOFTEER;

import java.io.*;
import java.util.*;

class 택배마스터광우 {
    static Map<Character, String> map = new HashMap<>();
    private static boolean[] visited = new boolean[10];
    private static int[] matrix = new int[10];
    private static int result = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nmk = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        int n = nmk[0], m = nmk[1], k = nmk[2];
        
        int[] weights = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();

        dfs(n, m, k, weights, 0);
        
        System.out.println(result);
        br.close();
    }

    // dfs로 모든 순열을 생성
    private static void dfs(int n, int m, int k, int[] weights, int count) {
        // 순열이 완성되었다면 m 이하로 묶어서 계산한다.
        if (count == n) {
            int idx = 0;
            int bucket = 0;
            int sumOfData = 0;

            for (int work = 0; work < k; work++) {
                while (matrix[idx] + bucket <= m) {
                    bucket += matrix[idx];
                    idx = (idx + 1) % n;
                }
                sumOfData += bucket;
                bucket = 0;
            }
            result = Math.min(sumOfData, result);
            return;
        }
        // visited 배열을 통해 중복을 방지하고, matrix에 순서대로 저장한다.
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                matrix[count] = weights[i];
                dfs(n, m, k, weights, count + 1);
                visited[i] = false;
            }
        }
    }
}
