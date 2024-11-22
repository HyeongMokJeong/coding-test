package SOFTEER;

import java.io.*;
import java.util.*;

class 성적평가 {
    private static int contest = 3;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // n 입력
        int n = Integer.parseInt(br.readLine());

        // 각 인원 별 총 점수를 합산하기 위한 sumScores 배열 선언
        int[] sumScores = new int[n];
        // 각 대회의 결과 입력
        for (int i = 0; i < contest; i++) {
            int[] scores = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();
            for (int j = 0; j < n; j++) {
                sumScores[j] += scores[j];
            } 

            int[] ranks = run(n, scores);

            StringBuilder sb = new StringBuilder();
            for (int r : ranks) sb.append(r).append(" ");
            System.out.println(sb.toString());
        }

        StringBuilder sb = new StringBuilder();
        int[] ranks = run(n, sumScores);
        for (int r : ranks) sb.append(r).append(" ");
        System.out.println(sb.toString());
        
        br.close();
    }

    private static int[] run(int n, int[] scores) {
        int[] result = new int[n];

        // 최대 힙 활용
        Queue<int[]> maxHeap = new PriorityQueue<>(
            (a, b) -> Integer.compare(b[0], a[0])
        );

        for (int i = 0; i < n; i++) {
            maxHeap.offer(new int[]{scores[i], i});
        }

        int rank = 1;
        int rankTemp = 0;
        int beforeScore = -1;
        while (!maxHeap.isEmpty()) {
            int[] target = maxHeap.poll();
            int score = target[0], idx = target[1];
            // 이전 점수와 같다면(동일 순위라면) 
            if (score == beforeScore) {
                // rank 부여 후 rankTemp + 1
                result[idx] = rank;
                rankTemp += 1;
            } else {
                // 다르다면 rankTemp의 다음 순위를 rank에 저장, 부여
                rank = rankTemp + 1;
                result[idx] = rank;
                rankTemp += 1;
                beforeScore = score;
            }
        }

        return result;
    }
}
