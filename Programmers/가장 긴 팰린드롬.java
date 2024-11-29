class Solution
{
    public int solution(String s)
    {
        int n = s.length();

        // 가장 긴 -> 최대 길이부터 줄여가며 확인
        // i = 길이, j = 시작 인덱스
        for (int i = n; i > 0; i--) {
            for (int j = 0; j + i <= n; j++) {
                if (check(s, j, j + i - 1)) return i; 
            }
        }

        return 0;
    }
    
    private boolean check(String target, int s, int e) {
        while (s <= e) {
            if (target.charAt(s++) != target.charAt(e--)) return false;
        }
        return true;
    }
}