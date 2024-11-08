package SOFTEER;

import java.io.*;
import java.util.*;

class 스마트물류 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // n, k 입력
        int[] nk = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        int n = nk[0], k = nk[1];

        // 라인 정보 입력 및 초기화
        char[] line = new char[n];
        String input = br.readLine();
        for(int i = 0; i < n; i++) line[i] = input.charAt(i);

        // 탐색 흐름이 -> 일 때, 각 로봇이 가장 왼쪽에 있는 부품을 집어야 최대가 됨
        int result = 0;
        for (int i = 0; i < n; i++) {
            if (line[i] == 'P') {
                for (int j = i - k; j <= i + k; j++) {
                    if (j < 0 || j >= n) continue;
                    if (line[j] == 'H') {
                        result += 1;
                        line[j] = '-';
                        break;
                    }
                }
            }
        }
        System.out.println(result);
        br.close();
    }
}
