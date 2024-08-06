import java.util.Collections;
import java.util.PriorityQueue;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;

        // 최대한 모든 값이 같게, 적게 줄인다.
        PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
        for (int work : works) q.offer(work);

        while (n-- > 0) {
            int target = q.poll();
            q.add((target == 0) ? 0 : target - 1);
        }
        while (!q.isEmpty()) answer += Math.pow(q.poll(), 2);

        return answer;
    }
}