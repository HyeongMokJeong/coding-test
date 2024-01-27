import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        int size = want.length;
        Map<String, Integer> maps = new HashMap<>();
        
        for (int i = 0; i < size; i++) maps.put(want[i], number[i]);
        for (int i = 0; i < 10; i++) {
            if (!maps.containsKey(discount[i])) continue;
            maps.put(discount[i], maps.get(discount[i]) - 1);
        }
        int temp = 0;
        for (Integer value : maps.values()) if (value <= 0) temp += 1;
        if (temp == size) answer += 1;

        int lp = 0, rp = 10;
        while (discount.length > rp) {
            String left = discount[lp], right = discount[rp];
            if (maps.containsKey(left)) {
                if (maps.get(left) == 0) temp -= 1;
                maps.put(left, maps.get(left) + 1);
            }
            if (maps.containsKey(right)) {
                if (maps.get(right) == 1) temp += 1;
                maps.put(right, maps.get(right) - 1);
            }
            if (temp == size) answer += 1;
            lp ++;
            rp ++;
        }
        
        return answer;
    }
}