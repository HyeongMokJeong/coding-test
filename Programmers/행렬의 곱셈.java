class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        int x = arr1.length, y = arr2[0].length, z = arr1[0].length;
        int[][] answer = new int[x][y];
        
        // arr1의 행
        for (int i = 0; i < x; i++) {
            // arr2의 열
            for (int j = 0; j < y; j++) {
                int temp = 0;
                // arr1의 열
                for (int k = 0; k < z; k++) {
                    temp += arr1[i][k] * arr2[k][j];
                }
                answer[i][j] = temp;
            }
        }
        return answer;
    }
}