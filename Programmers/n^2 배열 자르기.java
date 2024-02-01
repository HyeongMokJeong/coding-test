class Solution {
    public int[] solution(int n, long left, long right) {
        int[] answer = new int[(int) (right - left) + 1];

        for (int i = 0; i < answer.length; i++) {
            // x, y 좌표를 구하고 max(x, y)가 해당 위치의 값
            int y = (int) (left / n + 1);
            int x = (int) (left % n + 1);
            left++;
            answer[i] = Math.max(y, x);
        }
        return answer;
    }
}