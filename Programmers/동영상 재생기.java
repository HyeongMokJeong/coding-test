class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        int vl = stringToInt(video_len), p = stringToInt(pos);

        for (String command : commands) {
            if (p >= stringToInt(op_start) && p <= stringToInt(op_end)) p = stringToInt(op_end);
            if (command.equals("next")) p = (p + 10 <= vl) ? p + 10 : vl;
            else p = (p - 10 >= 0) ? p - 10 : 0;
        }

        return (p >= stringToInt(op_start) && p <= stringToInt(op_end)) ? op_end : intToString(p);
    }

    private int stringToInt(String time) {
        String[] part = time.split(":");
        return Integer.parseInt(part[0]) * 60 + Integer.parseInt(part[1]);
    }

    private String intToString(int time) {
        return String.format("%02d:%02d", time / 60, time % 60);
    }
}