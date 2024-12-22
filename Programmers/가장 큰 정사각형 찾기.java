class Solution {
    private int[][] directions = {{0, -1}, {-1, 0}, {-1, -1}};
    
    public int solution(int [][]board) {
        int answer = 0;
        // 길이가 1이라면 0 or 1 return
        if (board.length == 1) {
            for (int[] bo : board) {
                for (int b : bo) if (b == 1) return 1;   
            }
            return 0;
        }
        
        // [1, 1] 좌표부터 좌, 좌상, 상 방향을 체크한다.
        // 만약 [i, j] 좌표가 0이 아니라면 세 방향 중 최소값(최소 크기)에 1을 더한다.
        for (int i = 1; i < board.length; i++) {
            for (int j = 1; j < board[0].length; j++) {
                if (board[i][j] == 0) continue;
                
                int minTemp = Integer.MAX_VALUE;
                for (int[] d : directions) {
                    int nx = i + d[0], ny = j + d[1];
                    
                    if (0 > nx || 0 > ny) continue;
                    minTemp = Math.min(minTemp, board[nx][ny]);
                }
                board[i][j] = (minTemp != Integer.MAX_VALUE) ? minTemp + 1 : 0;
                answer = Math.max(answer, board[i][j]);
            }
        }

        return answer * answer;
    }
}