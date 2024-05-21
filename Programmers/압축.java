import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int[] solution(String msg) {
        List<Integer> answer = new ArrayList<>();

        int mapCount = 27;
        Map<String, Integer> map = getDefaultMap();

        int idx = 0;
        while (idx < msg.length()) {
            String target = String.valueOf(msg.charAt(idx));
            int value = map.get(target);

            while (idx + 1 < msg.length() && map.containsKey(target + msg.charAt(idx + 1))) {
                idx += 1;
                target += msg.charAt(idx);
                value = map.get(target);
            }
            answer.add(value);

            if (idx + 1 < msg.length() && !map.containsKey(target + msg.charAt(idx + 1))) {
                map.put(target + msg.charAt(idx + 1), mapCount++);
            }

            idx++;
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }

    private Map<String, Integer> getDefaultMap() {
        Map<String, Integer> map = new HashMap<>();
        for (char c = 'A'; c <= 'Z'; c++) {
            map.put(String.valueOf(c), c - 'A' + 1);
        }
        return map;
    }
}