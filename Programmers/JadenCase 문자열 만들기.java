class Solution {
    public String solution(String s) {
        String answer = "";

        String[] sp = s.split(" ");

        for (String spu : sp) answer += run(spu);

        return (s.charAt(s.length() - 1) == ' ')
            ? answer
            : answer.substring(0, answer.length() - 1);
    }

    private String run(String target) {
        if(target.length() == 0) return " ";

        StringBuilder sb = new StringBuilder();

        sb.append(target.substring(0, 1).toUpperCase());
        sb.append(target.substring(1, target.length()).toLowerCase());
        sb.append(" ");

        return sb.toString();
    }
}