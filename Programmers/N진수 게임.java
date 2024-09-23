class Solution {
    public String solution(int n, int t, int m, int p) {
        String answer = "";

        int target = 0, count = 1;
        while (answer.length() < t) {
            String stringTarget = Integer.toString(target, n).toUpperCase();

            for (int i = 0; i < stringTarget.length(); i++) {
                if (count == p) answer += stringTarget.charAt(i);
                if (answer.length() >= t) break;
                count = count % m + 1;
            }
            target += 1;
        }

        return answer;
    }
}