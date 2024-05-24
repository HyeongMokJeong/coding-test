import java.util.ArrayDeque;

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];

        ArrayDeque<Integer> stack = new ArrayDeque<>();

        for (int i = 0; i < prices.length; i++) {
            while (!stack.isEmpty() && prices[stack.peek()] > prices[i]) {
                int target = stack.pop();
                answer[target] = i - target;
            }
            stack.push(i);
        }
        while (!stack.isEmpty()) {
            int target = stack.pop();
            answer[target] = prices.length - target - 1;
        }

        return answer;
    }
}