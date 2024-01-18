import java.util.HashMap;
import java.util.Map;

class Solution {
    public static int solution(int[] topping) {
        int answer = 0;
        int countLeft = 0, countRight = 0;
        Map<Integer, Integer> leftMap = new HashMap<>();
        Map<Integer, Integer> rightMap = new HashMap<>();

        for (int i : topping) {
            Integer value = rightMap.get(i);
            if (value == null) {
                rightMap.put(i, 1);
                countRight += 1;
            }
            else rightMap.put(i, value + 1);
        }
        
        for (int i : topping) {
            if (leftMap.get(i) == null) {
                leftMap.put(i, 1);
                countLeft += 1;
            }
            rightMap.put(i, rightMap.get(i) - 1);
            if (rightMap.get(i) == 0) countRight -= 1;

            if (countLeft == countRight) answer += 1;
        }
        return answer;
    }
}