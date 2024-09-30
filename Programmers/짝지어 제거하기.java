import java.util.ArrayDeque;

class Solution
{
    public int solution(String s)
    {
        ArrayDeque<Character> stack = new ArrayDeque<>();
        for (char target : s.toCharArray()) {
            if (!stack.isEmpty() && stack.peekLast() == target) stack.pollLast();
            else stack.addLast(target);
        }
        return (stack.isEmpty()) ? 1 : 0;
    }
}