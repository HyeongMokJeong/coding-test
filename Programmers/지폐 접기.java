class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        
        int minWalletSize = (wallet[0] > wallet[1]) ? wallet[1] : wallet[0];
        int maxWalletSize = (minWalletSize == wallet[0]) ? wallet[1] : wallet[0];
        int minBillSize = (bill[0] > bill[1]) ? bill[1] : bill[0]; 
        int maxBillSize = (minBillSize == bill[0]) ? bill[1] : bill[0];
        
        while (minBillSize > minWalletSize || maxBillSize > maxWalletSize) {
            maxBillSize /= 2;
            if (minBillSize > maxBillSize) {
                int temp = minBillSize;
                minBillSize = maxBillSize;
                maxBillSize = temp;
            }
            answer += 1;
        }
        
        return answer;
    }
}