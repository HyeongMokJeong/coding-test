package SOFTEER;

import java.io.*;
import java.util.*;

class 업무처리 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] hkr = Arrays.stream(br.readLine().split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        int h = hkr[0], k = hkr[1], r = hkr[2];

        int leaf = (int) Math.pow(2, h); // 리프노드 개수
        int n = (int) Math.pow(2, h + 1) - 1; // 전체노드 개수

        // tasks[i][0] = 왼쪽 / tasks[i][1] = 오른쪽
        Queue<Integer>[][] tasks = new Queue[n + 1][2];
        for(int i = 1; i <= n; i++){
            for(int j = 0; j < 2; j++){
                tasks[i][j] = new ArrayDeque<>();
            }
        }

        // 말단 직원들의 업무 분배
        for (int i = 1; i <= leaf; i++) {
            int[] work = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

            for (int w : work) {
                tasks[n - leaf + i][0].offer(w);
            }
        }

        // 날짜 r 동안 업무 처리
        int result = 0;

        for (int day = 1; day <= r; day++) {
            // 왼쪽, 오른쪽을 처리할 idx 변수
            // 0 = 짝수, 오른쪽 / 1 = 홀수, 왼쪽
            int idx = day % 2;
            
            // 부서장 처리
            if (!tasks[1][idx].isEmpty()) {
                result += tasks[1][idx].poll();
            }

            // 중간 직원 처리
            for (int i = 2; i <= n - leaf; i++) {
                // 처리한 일이 있다면 부모에게로 전달
                if (!tasks[i][idx].isEmpty()) {
                    // 왼쪽 자식이라면 1, 오른쪽 자식이라면 0번 인덱스로 전달해야 함
                    tasks[i / 2][(i + 1) % 2].offer(tasks[i][idx].poll());
                }
            }

            // 말단 직원 처리
            for (int i = n - leaf + 1; i <= n; i++) {
                // 말단 직원의 업무는 0번 인덱스에 저장했음
                if (!tasks[i][0].isEmpty()) {
                    tasks[i / 2][(i + 1) % 2].offer(tasks[i][0].poll());  
                }
            }
        }

        System.out.println(result);
        br.close();
    }
}
