import java.util.*;

class Solution {
    public int solution(String str1, String str2) {
        List<String> str1Set = createSet(str1);
        List<String> str2Set = createSet(str2);

        List<String> unionSet = new ArrayList<>();
        List<String> interSet = new ArrayList<>();

        for (String target : str1Set) {
            if (str2Set.remove(target)) interSet.add(target);
            unionSet.add(target);
        }
        for (String target : str2Set) unionSet.add(target);

        double value = (unionSet.size() == 0) ? 1 : (double) interSet.size() / (double) unionSet.size();

        return (int)(value * 65536);
    }

    private List<String> createSet(String target) {
        ArrayList<String> result = new ArrayList<>();
        target = target.toLowerCase();

        for (int i = 0; i < target.length() - 1; i++) {
            char t = target.charAt(i); char n = target.charAt(i + 1);
            if ('a' <= t && t <= 'z' && 'a' <= n && n <= 'z') result.add(t + "" + n);
        }
        return result;
    }
}