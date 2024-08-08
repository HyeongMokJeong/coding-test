import java.util.Collections;
import java.util.PriorityQueue;

class Solution {
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> maxQ = new PriorityQueue<>(Collections.reverseOrder());
        PriorityQueue<Integer> minQ = new PriorityQueue<>();

        for (String op : operations) {
            String[] s = op.split(" ");

            if (s[0].equals("I")) {
                maxQ.offer(Integer.valueOf(s[1]));
                minQ.offer(Integer.valueOf(s[1]));
            } else {
                if (s[1].equals("1") && !maxQ.isEmpty()) minQ.remove(maxQ.poll());
                else if (s[1].equals("-1") && !minQ.isEmpty()) maxQ.remove(minQ.poll());
            }
        }

        int min = minQ.isEmpty() ? 0 : minQ.poll();
        int max = maxQ.isEmpty() ? 0 : maxQ.poll();

        return new int[]{max, min};
    }
}