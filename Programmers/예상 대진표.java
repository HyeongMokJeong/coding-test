class Solution {
    public int solution(int n, int a, int b) {
        int answer = 1;
        if (a > b) {
            int temp = b;
            b = a;
            a = temp;
        }

        while (!(b % 2 == 0 && b - 1 == a)) {
            a = a / 2 + a % 2;
            b = b / 2 + b % 2;
            answer += 1;
        }

        return answer;
    }
}