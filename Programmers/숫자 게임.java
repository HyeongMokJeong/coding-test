import java.util.Arrays;

class Solution {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        int index = A.length - 1;

        Arrays.sort(A);
        Arrays.sort(B);
        for(int i = A.length - 1; i >= 0; i--) {
            if(B[index] > A[i]) {
                answer++;
                index--;
            }
        }
        return answer;
    }
}