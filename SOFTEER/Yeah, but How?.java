package SOFTEER;

import java.io.*;
import java.util.*;

class YeahButHow {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] s = br.readLine().split("");

        // 순서대로 확인하기 위해 큐 사용
        Deque<String> q = new ArrayDeque<>();
        for (String target : s) q.offer(target);

        StringBuilder sb = new StringBuilder();
        while (!q.isEmpty()) {
            String target = q.poll();

            // 여는 괄호 "("인 경우
            if (target.equals("(")) {
                // 닫는 괄호 ")" 사이라면 1 또는 1+1.. 을 삽입
                if (q.peek().equals(")")) sb.append(target + "1");
                // 또 다시 여는 괄호 "(" 라면 그대로 추가
                else sb.append(target);
            } 
            // 닫는 괄호 ")"인 경우
            else {
                // 마지막이거나 또 다시 닫는 괄호 ")" 라면 그대로 추가
                if (q.peek() == null || q.peek().equals(")")) sb.append(target);
                // 여는 괄호 "(" 인 경우 연결하기 위해 + 삽입
                else sb.append(target + "+");
            }
        }

        System.out.println(sb.toString());
        br.close();
    }
}
