package SOFTEER;

import java.io.*;
import java.util.*;

class PS {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String[] a = br.readLine().split(" ");

        // 왼쪽을 체크할 stack과 현재부터 오른쪽을 체크할 queue 선언
        Deque<long[]> stack = new ArrayDeque<>();
        Deque<long[]> queue = new ArrayDeque<>();
        for (int i = 0; i < n; i++) queue.offer(new long[]{i + 1, Long.parseLong(a[i])});
        
        // 남은 미생물이 1개일 때까지 매 초
        while (queue.size() > 1) {
            // 모든 미생물이 활동할 동안
            while (!queue.isEmpty()) {
                // 현재 타켓 미생물을 poll
                long[] target = queue.poll();
                long tempSize = target[1];

                // 왼쪽에 미생물이 있다면
                if (!stack.isEmpty()) {
                    long[] left = stack.peekLast();

                    // 크기 비교 후 흡수
                    if (left[1] <= target[1]) {
                        tempSize += left[1];
                        stack.pollLast();
                    }
                }
                // 오른쪽에 미생물이 있다면
                if (!queue.isEmpty()) {
                    long[] right = queue.peek();

                    // 크기 비교 후 흡수
                    if (right[1] <= target[1]) {
                        tempSize += right[1];
                        queue.poll();
                    }
                }

                // 흡수한 결과를 스택에 추가
                stack.offerLast(new long[]{target[0], tempSize});
            }

            // 하루에 한 번 활동한 이후의 결과를 다시 queue에 저장하고 반복
            queue = stack;
            stack = new ArrayDeque<>();
        }
        long[] result = queue.poll();
        System.out.println(result[1]);
        System.out.println(result[0]);
        br.close();
    }
}
