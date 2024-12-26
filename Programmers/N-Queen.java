class Solution {
    private int[] board;
    private int answer;
    public int solution(int n) {
        // 각 행, 열에 하나의 퀸만 존재할 수 있다.
        // 따라서 1차원 배열로 압축할 수 있다.
        // 배열의 각 인덱스는 y좌표(열)을 의미하고, 값은 x좌표(행)을 의미한다.
        board = new int[n];
        bt(0, n);

        return answer;
    }

    // depth가 열을 의미한다.
    private void bt(int depth, int n) {
        // 만약 n개의 퀸을 설치했다면
        if (depth == n) {
            answer += 1;
            return;
        }

        // 아직이라면 설치한 후, 유효한지 확인한다.
        for (int i = 0; i < n; i++) {
            board[depth] = i;
            if (check(depth)) bt(depth + 1, n);
        }
    }

    private boolean check(int idx) {
        // idx번째에 퀸을 놓았으니, 그 이전 퀸들과 비교하며 유효성을 검증한다.
        for (int i = 0; i < idx; i++) {
            // 값이 같다면 같은 행이라는 뜻이므로 유효하지 않다.
            if (board[i] == board[idx]) return false;
            // 열의 차이 = 행의 차이라면 기울기가 1이라는 뜻이므로 유효하지 않다.
            if (Math.abs(i - idx) == Math.abs(board[i] - board[idx])) return false;
        }
        return true;
    }
}