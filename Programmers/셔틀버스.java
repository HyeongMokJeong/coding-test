import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

class Solution {
    public String solution(int n, int t, int m, String[] timetable) {
        String answer = "";

        PriorityQueue<Integer> q = new PriorityQueue<>();
        for (String time : timetable) q.offer(convertToInt(time));

        // n번 운행하는 버스 리스트
        List<Integer>[] bus = new ArrayList[n];
        for (int i = 0; i < n; i++) bus[i] = new ArrayList<>();

        int temp = 0;
        int aliveTime = 9 * 60;
        for (int i = 0; i < n; i++) {
            while (!q.isEmpty()) {
                int target = q.poll();

                if (bus[i].size() < m && target <= aliveTime) {
                    bus[i].add(target);
                    temp = target - 1; // 마지막 탑승자라면 더 빨리와야 출근 가능, 마지막이 아닌 경우는 아래에서 처리
                } else {
                    q.offer(target);
                    break;
                }
            }
            aliveTime += t;
        }

        if (bus[n - 1].size() < m) temp = aliveTime - t;

        return String.format("%02d", temp / 60)
        + ":" 
        + String.format("%02d", temp % 60);
    }

    private int convertToInt(String time) {
        String[] ary = time.split(":");
        return Integer.parseInt(ary[0]) * 60 + Integer.parseInt(ary[1]);
    }
}