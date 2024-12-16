class Solution {
    private String[] num = {"4", "1", "2"};
    private int size = num.length;
    
    public String solution(int n) {
        StringBuilder sb = new StringBuilder();
        
        while (n > 0) {
            int next = n % size;
            sb.insert(0, num[next]);
            if (next == 0) n -= 1;
            n /= size;
        }
        
        return sb.toString();
    }
}