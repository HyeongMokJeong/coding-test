import java.util.*;

class Solution {
    boolean solution(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char c : s.toCharArray()) {
            // 여는 괄호
            if (c == '(') {
                stack.addLast(c);
            } 
            // 닫는 괄호
            else {
                if (stack.isEmpty()) return false;
                if (stack.peekLast() == '(') stack.pollLast();
                else stack.addLast(c);
            }
        }

        return stack.isEmpty();
    }
}