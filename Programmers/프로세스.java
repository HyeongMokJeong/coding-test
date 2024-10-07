import java.util.PriorityQueue;
import java.util.ArrayDeque;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1;

        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> b - a);
        for (int i = 0; i < priorities.length; i++) pq.offer(priorities[i]);
        
        ArrayDeque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < priorities.length; i++) q.offer(i);

        while (!q.isEmpty()) {
            int target = q.poll();

            if (priorities[target] != pq.peek()) q.offer(target);
            else {
                if (target == location) return answer;
                pq.poll();
                answer += 1;
            }
        }

        return answer;
    }
}