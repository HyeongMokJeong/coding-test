import java.util.Arrays;

class Solution {
    public int solution(int[][] routes) {
        Arrays.sort(routes, (a, b) -> Integer.compare(a[1], b[1]));

        int answer = 1;
        int end = routes[0][1];
        for (int[] route : routes) {
            if (route[0] > end) {
                answer += 1;
                end = route[1];
            }
        }

        return answer;
    }
}