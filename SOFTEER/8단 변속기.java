package SOFTEER;

import java.io.*;
import java.util.*;

class 나무섭지 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // int 배열로 변환
        int[] numbers = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();

        // result가 true라면 오름차순, false라면 내림차순
        boolean result = numbers[0] < numbers[1];
        for (int i = 1; i < numbers.length - 1; i++) {
            boolean c = numbers[i] < numbers[i + 1];

            // 만약 다른 흐름이 발생하면 mixed 출력 후 탈출
            if (result != c) {
                System.out.println("mixed");
                return;
            }
        }
        System.out.println((result) ? "ascending" : "descending");
        br.close();
    }
}
