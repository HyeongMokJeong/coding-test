class Solution {
    String answer = null;
    StringBuilder route;
    char[] dir = {'d', 'l', 'r', 'u'};
    int[] dx = {1, 0, 0, -1}; int[] dy = {0, -1, 1, 0};
    int endX; int endY;

    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        route = new StringBuilder();
        endX = r; endY = c;

        int length = distance(x, y, r, c);
        if((k - length) % 2 == 1 || k < length) return "impossible";
        dfs(n, m, x, y, 0, k);
        
        return answer == null ? "impossible" : answer;
    }

    private void dfs(int n, int m, int x, int y, int count, int k) {
        if(answer != null) return;
        if(count + distance(x, y, endX, endY) > k) return;
        if(k == count) {
            answer = route.toString();
            return;
        }
        for(int i = 0; i < 4; i++){
            int nx = x + dx[i]; int ny = y + dy[i];
            if((0 < nx && nx <= n) && (0 < ny && ny <= m)){
                route.append(dir[i]);
                dfs(n, m, nx, ny, count + 1, k);
                route.deleteCharAt(count);
            }
        }
    }

    private int distance(int x, int y, int r, int c){
        return (int)Math.abs(x - r) + (int)Math.abs(y - c);
    }
}