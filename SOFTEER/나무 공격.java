package SOFTEER;

import java.io.*;
import java.util.*;

class 나무공격 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] nm = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        int n = nm[0];

        // 파괴범 수를 미리 세기 위한 result와 각 행에 몇 명이 있는지 체크할 countAry 초기화
        int result = 0;
        int[] countAry = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            String[] input = br.readLine().split(" ");

            int count = 0;
            for (String inp : input) {
                if (inp.equals("1")) {
                    count += 1;
                    result += 1;
                }
            }
            countAry[i] = count;
        }

        // L R을 입력받아 공격 시작
        int attckSize = 2;
        for (int i = 0; i < attckSize; i++) {
            int[] lr = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            int l = lr[0], r = lr[1];

            for (int j = l; j <= r; j++) {
                if (countAry[j] > 0) {
                    countAry[j] -= 1;
                    result -= 1;
                }
            }
        }

        System.out.println(result);
        br.close();
    }
}
