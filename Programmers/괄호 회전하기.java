import java.util.Stack;

class Solution {
    private int check(String s) {
        Stack<Character> stack = new Stack<>();

        for (char t : s.toCharArray()) {
            if (t == '(' || t == '{' || t == '[') stack.push(t);
            else {
                if (stack.isEmpty()) return 0;
                char left = stack.pop();
                if (left == '(' && t == ')') continue;
                if (left == '[' && t == ']') continue;
                if (left == '{' && t == '}') continue;
                return 0;
            }
        }
        return stack.isEmpty() ? 1 : 0;
    }
    public int solution(String s) {
        int answer = 0;
        for (int i = 0; i < s.length(); i++) {
            answer += check(s);
            s = s.substring(1) + s.charAt(0);
        }
        return answer;
    }
}