import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.TreeSet;

import javax.swing.RowFilter.Entry;

class Solution {
    private int getMinute(String formatString) {
        String[] hm = formatString.split(":");
        return Integer.parseInt(hm[0]) * 60 + Integer.parseInt(hm[1]);
    }

    private void checkList(Map<String, Integer> accMap, Map<String, Integer> tempMap, String[] records) {
        for (String record : records) {
            String[] part = record.split(" ");
            String time = part[0], target = part[1];
            if (tempMap.get(target) == null) tempMap.put(target, getMinute(time));
            else {
                int before = accMap.getOrDefault(target, 0);
                accMap.put(target, before + getMinute(time) - tempMap.get(target));
                tempMap.put(target, null);
            }
        }

        for (Map.Entry<String, Integer> entry : tempMap.entrySet()) {
            if (entry.getValue() != null) {
                accMap.put(entry.getKey(), accMap.getOrDefault(entry.getKey(), 0) + (23 * 60 + 59) - entry.getValue());
            }
        }
    }

    private int[] caluclateList(int[] fees, Map<String, Integer> accMap) {
        List<Integer> answer = new LinkedList<>();

        List<String> numberList = new ArrayList<>(new TreeSet<>(accMap.keySet()));
        for (String target : numberList) {
            int before = accMap.get(target);
            if (before <= fees[0]) answer.add(fees[1]);
            else answer.add(fees[1] + (int) Math.ceil(((double) before - (double) fees[0]) / fees[2]) * fees[3]);
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }

    public int[] solution(int[] fees, String[] records) {
        Map<String, Integer> accMap = new HashMap();
        Map<String, Integer> tempMap = new HashMap();
        checkList(accMap, tempMap, records);

        List<String> numberList = new ArrayList<>(new TreeSet<>(accMap.keySet()));
        
        return caluclateList(fees, accMap);
    }
}