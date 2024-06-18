import java.util.ArrayDeque;

class Solution {
    public String[] solution(String[] s) {
        String[] answer = new String[s.length];

        for (int idx = 0; idx < s.length; idx++) {
            ArrayDeque<Character> stack = new ArrayDeque<>();
            int count = 0;

            for (int i = 0; i < s[idx].length(); i++) {
                stack.addLast(s[idx].charAt(i));

                if (stack.size() >= 3) {
                    char first = stack.pollLast();
                    if (first != '0') {
                        stack.addLast(first);
                        continue;
                    }

                    char second = stack.pollLast();
                    if (second != '1') {
                        stack.addLast(second);
                        stack.addLast(first);
                        continue;
                    }

                    char third = stack.pollLast();
                    if (third != '1') {
                        stack.addLast(third);
                        stack.addLast(second);
                        stack.addLast(first);
                        continue;
                    }

                    count++;
                }
            }

            int lastZeroIndex = -1;

            StringBuilder sb = new StringBuilder();
            int index = 0;
            while (!stack.isEmpty()) {
                char t = stack.pollFirst(); 
                sb.append(t);
                if (t == '0') lastZeroIndex = index;
                index++;
            }

            StringBuilder insertSb = new StringBuilder();
            while (count-- > 0) insertSb.append("110");
            String insertString = insertSb.toString();

            sb.insert(lastZeroIndex + 1, insertString);
            answer[idx] = sb.toString();
        }
        return answer;
    }
}