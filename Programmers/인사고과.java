import java.util.Arrays;

class Solution {
    public int solution(int[][] scores) {
        int answer = 1;
        int a = scores[0][0]; int b = scores[0][1];

        Arrays.sort(scores, (o1, o2) -> {
            if (o1[0] < o2[0]) return 1;
            else if (o1[0] == o2[0]) return o1[1] > o2[1] ? 1 : -1;
            else return -1;
        });

        int minB = 0;
        for (int[] score : scores) {
            if (score[1] < minB) {
                if (score[0] == a && score[1] == b) return -1;
            }
            else {
                minB = Math.max(minB, score[1]);
                if (score[0] + score[1] > a + b) answer++;
            }
        }
        return answer;
    }
}