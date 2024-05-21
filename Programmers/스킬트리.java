import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;

        Map<Character, Integer> skillMap = new HashMap<>();
        int i = 0;
        for (char c : skill.toCharArray()) {
            skillMap.put(c, i);
            i++;
        }

        for (String target : skill_trees) {
            int count = 0;
            boolean check = false;
            for (char c : target.toCharArray()) {
                if (skillMap.containsKey(c)) {
                    Integer number = skillMap.get(c);
                    if (number > count) {
                        check = true;
                        break;
                    }
                    else if (number == count) count++;
                }
            }
            if (!check) answer++;
        }

        return answer;
    }
}