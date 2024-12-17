class Solution {
    public int solution(int n) {
        // 2진수 표현에서 1의 개수를 세는 메서드
        int countN = Integer.bitCount(n);
        
        int answer = n + 1;
        while (Integer.bitCount(answer) != countN) {
            answer += 1;
        }
        
        return answer;
    }
}