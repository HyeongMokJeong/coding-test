import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0, 0};

        String temp = null;
        Map<String, Boolean> countMap = new HashMap<>();
        for (int roop = 0; roop < words.length / n; roop++) {
            for (int i = 0; i < n; i++) {
                int idx = roop * n + i;

                String target = words[idx];
                if (temp == null) temp = target;
                else if (
                    temp.charAt(temp.length() - 1) != target.charAt(0)
                    || countMap.containsKey(target)
                ) {
                    return new int[]{i + 1, roop + 1};
                }

                temp = target;
                countMap.put(target, true);
            }
        }

        return answer;
    }
}