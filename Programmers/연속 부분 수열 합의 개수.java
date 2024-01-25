import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(int[] elements) {
        Set<Integer> result = new HashSet<>();
        int length = elements.length;

        for (int start = 1; start <= length; start++) {
            for (int i = 0; i < length; i++) {
                int temp = 0;
                for (int j = 0; j < start; j++) temp += elements[(i + j) % length]; 
                result.add(temp);
            }
        }
        return result.size();
    }
}