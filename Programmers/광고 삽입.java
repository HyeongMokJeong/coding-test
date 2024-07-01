import java.util.Arrays;

class Solution {
    public String solution(String play_time, String adv_time, String[] logs) {
        long[] temp = new long[convertTime(play_time) + 1];
        Arrays.fill(temp, 0);

        for (String log : logs) {
            String[] part = log.split("-");
            temp[convertTime(part[0])]++;
            temp[convertTime(part[1])]--;
        }
        // 해당 시점에 몇 명이 시청중인지
        for (int i = 1; i < temp.length; i++) temp[i] += temp[i - 1];
        // 해당 시점의 누적 시청시간
        for (int i = 1; i < temp.length; i++) temp[i] += temp[i - 1];
        
        int advDuration = convertTime(adv_time);
        long maxView = temp[advDuration - 1];
        int maxStartTime = 0;

        for (int i = advDuration; i < temp.length; i++) {
            long currentView = temp[i] - temp[i - advDuration];
            if (currentView > maxView) {
                maxView = currentView;
                maxStartTime = i - advDuration + 1;
            }
        }

        return reconvertTime(maxStartTime);
    }

    private int convertTime(String time) {
        String[] part = time.split(":");
        return 3600 * Integer.parseInt(part[0])
             + 60 * Integer.parseInt(part[1])
             + Integer.parseInt(part[2]);
    }

    private String reconvertTime(long time) {
        long hour = time / 3600;
        time %= 3600;
        long min = time / 60;
        long sec = time % 60;

        return String.format("%02d:%02d:%02d", hour, min, sec);
    }
}