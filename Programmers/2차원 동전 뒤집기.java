class Solution {
    private int[][] b, t;
    private int x, y;
    private int answer = Integer.MAX_VALUE;
    
    public int solution(int[][] beginning, int[][] target) {
        b = beginning; t = target;
        x = beginning.length; y = beginning[0].length;
        
        // 1. 행을 뒤집는 모든 경우를 구한다. (제한사항 상 최대 2^10 가지)
        // 2. 1의 결과를 순회하며 열을 뒤집어본다.
        // 2-1. 열이 전부 다르다면 -> 뒤집어서 맞출 수 있다.
        // 2-2. 열이 전부 같다면 -> 그대로 유지한다.
        // 2-3. 일부만 다르다면 -> 절대 맞출 수 없다.
        
        dfs(0, 0);
        return (answer == Integer.MAX_VALUE) ? -1 : answer;
    }
    
    // 행을 뒤집는다.
    private void swapRow(int r) {
        for (int i = 0; i < y; i++) {
            b[r][i] = (b[r][i] == 0) ? 1 : 0;
        }
    }
    
    // 열의 상태를 확인한다.
    private int checkCol(int c) {
        // 0이면 뒤집지 않음(이미 같음), 1이면 뒤집어야 함
        int start = (b[0][c] == t[0][c]) ? 0 : 1;
        
        for (int i = 1; i < x; i++) {
            int checkTarget = (b[i][c] == t[i][c]) ? 0 : 1;
            
            // 열을 뒤집는 것으로 맞출 수 없다면 -1
            if (start != checkTarget) return -1;
        }
        
        return start;
    }
    
    // 각 행의 인덱스 r, 뒤집은 횟수를 임시로 저장할 temp
    private void dfs(int r, int temp) {
        // 모든 행의 경우의 수를 확인했다면
        if (r == x) {
            // 각 열을 확인한다.
            int swapColCount = 0;
            
            for (int i = 0; i < y; i++) {
                int result = checkCol(i);
                
                // 만약 불가능하다면 종료
                if (result == -1) return;
                swapColCount += result;
            }
            
            answer = Math.min(answer, temp + swapColCount);
        } else {
            // r행을 뒤집지 않고 dfs
            dfs(r + 1, temp);
            // r행을 뒤집고 dfs
            swapRow(r);
            dfs(r + 1, temp + 1);
            swapRow(r);
        }
    }
}