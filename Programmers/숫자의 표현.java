class Solution {
    public int solution(int n) {
        int answer = 0;
        
        // n을 연속된 자연수의 합으로 표현할 수 있는 경우의 수 = n의 홀수 약수 개수
        for (int i = 1; i <= n; i += 2) if (n % i == 0) answer++;
        return answer;
    }

    class Solution2 {
        public int solution(int n) {
            int answer = 0;
            
            for (int i = 1; i <= n; i++) {
                int temp = 0;
                for (int j = i; j <= n; j++) {
                    temp += j;
                    
                    if (temp >= n) {
                        if (temp == n) answer += 1;
                        break;
                    }
                }
            }
            return answer;
        }
    }
}