package SOFTEER;

import java.io.*;

class 연탄의크기 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] houes = new int[n];

        // int 배열로 전환하며 최댓값 추출
        int maxTemp = 0;
        String[] input = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            int target = Integer.parseInt(input[i]);
            maxTemp = Math.max(maxTemp, target);
            houes[i] = target;
        }

        // 최댓값까지 순회하며 가장 많은 경우 파악
        int result = 0;
        for (int i = 2; i <= maxTemp; i++) {
            int temp = 0;
            for (int h : houes) {
                if (h % i == 0) temp += 1;
            }
            result = Math.max(result, temp);
        }

        System.out.println(result);
        br.close();
    }
}
