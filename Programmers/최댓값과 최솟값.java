import java.util.ArrayList;
import java.util.List;

class Solution {
    public String solution(String s) {
        String[] ary = s.split(" ");
        List<Integer> intList = new ArrayList<>();
        for (String target : ary) intList.add(Integer.parseInt(target));
        intList.sort(Integer::compare);

        return intList.get(0) + " " + intList.get(intList.size() - 1);
    }
}