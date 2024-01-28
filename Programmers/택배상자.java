import java.util.Stack;

class Solution {
    public int solution(int[] order) {
        int answer = 0;
        Stack<Integer> mainContainer = new Stack<>();
        Stack<Integer> subContainer = new Stack<>();

        for (int i = order.length; i > 0 ; i--) mainContainer.push(i);
        
        for (int target : order) {
            while (!mainContainer.isEmpty() && mainContainer.peek() < target) subContainer.push(mainContainer.pop());
            if (!mainContainer.isEmpty() && mainContainer.peek() == target) {
                mainContainer.pop();
                answer += 1;
                continue;
            }
            if (!subContainer.isEmpty() && subContainer.peek() == target) {
                subContainer.pop();
                answer += 1;
                continue;
            }
            break;
        }
        return answer;
    }
}