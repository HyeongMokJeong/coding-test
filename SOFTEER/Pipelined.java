package SOFTEER;

import java.io.*;
import java.util.*;

class Pipelined {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] steps = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();

        // 하나의 자동차는 처리되기 위해 s초가 필요
        // 오름차순으로 처리하는 경우, 1초마다 하나씩 작업 슬롯에 배치됨 (n - 1)
        // -> s가 가장 큰 자동차는 n - 1초 이후에 작업 슬롯에 배치되어 시작
        int maxValue = 0;
        for (int s : steps) maxValue = Math.max(maxValue, s);

        System.out.println(maxValue + n - 1);
        br.close();
    }
}
