class Solution {
    public long solution(int w, int h) {
        long answer = 0, x = (long) w, y = (long) h;
        for (int i = 1; i < x; i++) answer += y * i / x;
        return answer * 2;
    }
}