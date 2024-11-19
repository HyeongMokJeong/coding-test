package SOFTEER;

import java.io.*;
import java.util.*;

class 비밀메뉴2 {
    private static int[] a, b;
    private static int[][] dp;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // nmk 입력
        int[] nmk = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        int n = nmk[0], m = nmk[1], k = nmk[2];
        dp = new int[n][m];

        // a,b 배열 초기화
        a = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();

        b = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();

        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                result = Math.max(dfs(i, j), result);
            }
        }

        System.out.println(result);
        br.close();
    }

    // a, b 각 인덱스가 i, j일 때, 그 직전까지의 연속 공통 수열의 길이를 알면 된다.
    private static int dfs(int i, int j) {
        // 범위를 벗어나면 0
        if(i < 0 || j < 0) return 0;
        // 이전 값을 발견했다면 즉시 return
        if(dp[i][j] != 0) return dp[i][j];
        // 값이 없는데 자리가 같다면 갱신
        if(a[i] == b[j]) return dp[i][j] = 1 + dfs(i - 1, j - 1);
        return dp[i][j];
    }
}
