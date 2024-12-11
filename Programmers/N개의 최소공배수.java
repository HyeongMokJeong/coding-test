class Solution {
    public int solution(int[] arr) {
        int answer = arr[0];
        
        // 최소공배수 : (a * b) / (두 수의 최대공약수)
        for (int i = 1; i < arr.length; i++) {
            answer = (answer * arr[i]) / gcd(answer, arr[i]);
        }
        
        return answer;
    }
    
    // 두 수의 최소공약수를 구하는 유클리드 호제법
    // a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면, a와 b의 최대공약수는 b와 r의 최대공약수이다.
    private int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }
}