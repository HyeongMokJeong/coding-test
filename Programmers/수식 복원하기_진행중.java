import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    public String[] solution(String[] expressions) {
        List<String> exp = new ArrayList<>();
        List<String> nExp = new ArrayList<>();

        for (String e : expressions) {
            if (e.endsWith("X")) nExp.add(e);
            else exp.add(e);
        }

        // 가능한 진법을 추린다
        int start = checkStart(expressions), end = 9;
        Set<Integer> candidate = new HashSet<>();
        candidate.addAll(check(start, end, exp));

        String[] answer = new String[nExp.size()];
        // X 수식에 대입해본다.
        for (int i = 0; i < nExp.size(); i++) answer[i] = run(candidate, nExp.get(i));
        return answer;
    }
    
    private int checkStart(String[] exp) {
        int result = 2;
        for (String e : exp) {
            String[] parts = e.split("[^0-9]+");
            for (String part : parts) {
                result = Math.max(result, Integer.parseInt(part) % 10 + 1);
            }
        }
        return result;
    }

    private List<Integer> check(int start, int end, List<String> target) {
        Map<Integer, Integer> tempMap = new HashMap<>();
        for (String t : target) {
            boolean isAdd;
            String[] splitTarget;

            if (t.contains(" + ")) {
                isAdd = true;
                splitTarget = t.split(" \\+ ");
            } else {
                isAdd = false;
                splitTarget = t.split(" - ");
            }
            String[] splitTarget2 = splitTarget[1].split(" = ");

            String a = splitTarget[0];
            String b = splitTarget2[0];
            String c = splitTarget2[1];

            for (int i = start; i <= end; i++) {
                if (isAdd) {
                    if (Integer.parseInt(a, i) + Integer.parseInt(b, i) == Integer.parseInt(c, i)) {
                        tempMap.put(i, tempMap.getOrDefault(i, 0) + 1);
                    }
                } else {
                    if (Integer.parseInt(a, i) - Integer.parseInt(b, i) == Integer.parseInt(c, i)) {
                        tempMap.put(i, tempMap.getOrDefault(i, 0) + 1);
                    }
                }
            }
        }

        List<Integer> result = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : tempMap.entrySet()) {
            if (entry.getValue() >= target.size()) result.add(entry.getKey());
        }
        return result;
    }

    private String run(Set<Integer> candidate, String exp) {
        Map<Integer, Boolean> countMap = new HashMap<>();

        boolean isAdd;
        String[] splitTarget;
        if (exp.contains(" + ")) {
            isAdd = true;
            splitTarget = exp.split(" \\+ ");
        } else {
            isAdd = false;
            splitTarget = exp.split(" - ");
        }

        String a = splitTarget[0];
        String b = splitTarget[1].split(" = ")[0];

        for (int i : candidate) {
            if (isAdd) {
                countMap.put(Integer.parseInt(a, i) + Integer.parseInt(b, i), true); 
            } else {
                countMap.put(Integer.parseInt(a, i) - Integer.parseInt(b, i), true); 
            }
        }
 
        return (countMap.keySet().size() == 1) 
        ? exp.replaceAll("X", String.valueOf(countMap.keySet().iterator().next()))
        : exp.replaceAll("X", "?");
    }
}
