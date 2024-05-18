class Solution {
    public String solution(String p) {
        if (p.isEmpty()) return "";
        if (check(p)) return p;

        return run(p);
    }

    // 올바른 괄호 문자열 체크
    private boolean check(String target) {
        int left = 0; int right = 0;
        for (int i = 0; i < target.length(); i++) {
            if (target.charAt(i) == '(') left++;
            else right++;
            
            if (right > left) return false;
        }
        return true;
    }

    // 균형잡힌 괄호 문자열 분리
    private String run(String target) {
        if (target.isEmpty()) return "";

        int idx = 0;
        int countLeft = 0; int countRight = 0;

        while (idx < target.length()) {
            if (target.charAt(idx) == '(') countLeft++;
            else countRight++;
            if (countLeft == countRight) break;
            idx++;
        }

        String u = target.substring(0, idx + 1);
        String v = target.substring(idx + 1);

        if (check(u)) return u + run(v);
        else return "(" + run(v) + ")" + reverse(u);
    }

    private String reverse(String u) {
        StringBuilder sb = new StringBuilder();

        for (int i = 1; i < u.length() - 1; i++) {
            if (u.charAt(i) == '(') sb.append(')');
            else sb.append('(');
        }
        return sb.toString();
    }
}