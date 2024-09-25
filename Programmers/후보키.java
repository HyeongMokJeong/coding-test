import java.util.*;

class Solution {
    List<List<Integer>> combi = new ArrayList<>();

    public int solution(String[][] relation) {
        int answer = 0;
        List<Integer> notUnique = new ArrayList<>();

        for (int i = 0; i < relation[0].length; i++) {
            Set<String> temp = new HashSet<>();
            for (String[] r : relation) temp.add(r[i]);
            if (temp.size() == relation.length) answer += 1;
            else notUnique.add(i);
        }

        for (int i = 0; i < notUnique.size(); i++) {
            bt(notUnique, new ArrayList<>(Arrays.asList(notUnique.get(i))), i);
        }

        combi.sort(Comparator.comparingInt(List::size));

        List<List<Integer>> alive = new ArrayList<>();
        for (List<Integer> c : combi) {
            boolean flag = false;
            for (List<Integer> a : alive) {
                if (c.containsAll(a)) {
                    flag = true;
                    break;
                }
            }
            if (flag) continue;

            Set<String> temp = new HashSet<>();

            for (String[] r : relation) {
                String temp2 = "";
                for (int i = 0; i < c.size(); i++) temp2 += r[c.get(i)] + " ";
                temp.add(temp2); 
            }

            if (temp.size() == relation.length) {
                answer += 1;
                alive.add(c);
            }
        }

        return answer;
    }

    private void bt(List<Integer> notUnique, List<Integer> temp, int idx) {
        if (idx >= notUnique.size()) return;
        if (temp.size() > 1) combi.add(temp);

        for (int i = idx + 1; i < notUnique.size(); i++) {
            temp.add(notUnique.get(i));
            bt(notUnique, new ArrayList<>(temp), i);
            temp.remove(temp.size() - 1);
        }
    }
}