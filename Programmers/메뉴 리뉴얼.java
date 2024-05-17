import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public String[] solution(String[] orders, int[] course) {
        List<String> result = new ArrayList<>();

        for (int c : course) {
            Map<String, Integer> countMap = new HashMap<>();

            for (String order : orders) {
                char[] chars = order.toCharArray();
                Arrays.sort(chars);
                
                combination(countMap, chars, "", c, 0);
            }
            
            int maxValue = countMap.values().stream().mapToInt(Integer::intValue).max().orElse(0);
            if (maxValue < 2) continue;
            for (String key : countMap.keySet()) {
                if (countMap.get(key) == maxValue) result.add(key);
            }
        }

        Collections.sort(result);
        return result.toArray(new String[result.size()]);
    }

    private void combination(Map<String, Integer> countMap, char[] target, String targetString, int maxLength, int idx) {
        if (targetString.length() == maxLength) {
            countMap.put(targetString, countMap.getOrDefault(targetString, 0) + 1);
            return;
        }
        for (int i = idx; i < target.length; i++) {
            String nextString = targetString + target[i];
            combination(countMap, target, nextString, maxLength, i + 1);
        }
    }
}