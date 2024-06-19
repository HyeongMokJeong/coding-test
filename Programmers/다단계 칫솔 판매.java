import java.util.HashMap;
import java.util.Map;

class Solution {
    private Map<String, String> parentMap = new HashMap<>();
    private Map<String, Integer> countMap = new HashMap<>();

    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        int[] answer = new int[enroll.length];

        for (int i = 0; i < enroll.length; i++) parentMap.put(enroll[i], referral[i]);
        for (int i = 0; i < seller.length; i++) dfs(seller[i], amount[i] * 100);
        for (int i = 0; i < enroll.length; i++) answer[i] = countMap.getOrDefault(enroll[i], 0);

        return answer;
    }

    private void dfs(String target, int pay) {
        String parent = parentMap.get(target);

        int repay = pay / 10;
        countMap.put(target, countMap.getOrDefault(target, 0) + pay - repay);
        if (!parent.equals("-") && repay >= 1) dfs(parent, repay);
    }
}