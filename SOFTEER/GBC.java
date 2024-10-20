package SOFTEER;

import java.io.*;
import java.util.*;

class GBC {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int result = 0;

        int[] nm = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        int n = nm[0], m = nm[1];

        // 제한을 둘 배열 생성
        int idx = 0;
        int[] ary = new int[100];
        for (int i = 0; i < n; i++) {
            int[] ab = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            int a = ab[0], b = ab[1];

            for (int j = 0; j < a; j++) ary[idx++] = b;
        }

        // 구간만큼 갭 확인
        int tIdx = 0;
        for (int i = 0; i < m; i++) {
            int[] ab = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            int a = ab[0], b = ab[1];

            for (int j = 0; j < a; j++) {
                ary[tIdx] = b - ary[tIdx];
                result = Math.max(result, ary[tIdx]);
                tIdx += 1;
            }
        }
        System.out.println(result);
        br.close();
    }
}
