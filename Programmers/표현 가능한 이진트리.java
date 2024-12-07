import java.util.*;

class Solution {
    private boolean[] visitedDist;
    private int[] dist;
    private List<int[]> allWeak = new ArrayList<>();
    int answer = Integer.MAX_VALUE;
    
    public int solution(int n, int[] weak, int[] dist) {
        visitedDist = new boolean[dist.length];
        this.dist = dist;
        
        // 모든 weak 케이스를 만든다.
        // n = 12, weak = [1, 5, 6, 10]인 경우
        // [1, 5, 6, 10], [5, 6, 10, 13], [6, 10, 13, 17], [10, 13, 17, 18]
        // 한쪽 방향으로 탐색해도 모든 경우를 탐색할 수 있다.
        allWeak.add(weak.clone());
        for (int i = 1; i < weak.length; i++) {
            int temp = weak[0];
            for (int j = 0; j < weak.length - 1; j++) {
                weak[j] = weak[j + 1];
            }
            weak[weak.length - 1] = temp + n;
            allWeak.add(weak.clone());
        }
        
        // 모든 dist 케이스를 만든다.
        for (int i = 0; i < dist.length; i++) {
            int[] newDist = new int[dist.length];
            newDist[0] = dist[i];
            visitedDist[i] = true;
            dfs(1, newDist);
            visitedDist[i] = false;
        }
        
        
        return (answer == Integer.MAX_VALUE) ? -1 : answer;
    }
    
    private void dfs(int idx, int[] newDist) {
        if (idx == dist.length) {
            // 완성된 각 weak 케이스에 대해, 모든 dist 케이스를 검사한다.
            for (int[] w : allWeak) check(newDist, w);
            return;
        }
        for (int i = 0; i < dist.length; i++) {
            if (visitedDist[i]) continue;
            
            visitedDist[i] = true;
            newDist[idx] = dist[i];
            dfs(idx + 1, newDist);
            visitedDist[i] = false;
        }
    }
    
    private void check(int[] newDist, int[] targetWeak) {
        // cur = targetWeak idx
        int cur = 0, next;
        int distIdx = 0;
        
        while (cur < targetWeak.length && distIdx < newDist.length) {
            next = cur + 1;
            // targetWeak 범위 내이면서,
            // 현재 취약 좌표 + 현재 처리길이가 다음 취약점보다 크다면(커버 가능하다면) 다음 취약점 좌표 탐색
            while (next < targetWeak.length && 
                   targetWeak[cur] + newDist[distIdx] >= targetWeak[next]) next += 1;
            
            cur = next;
            distIdx += 1;
        }
        // 모든 취약점을 확인했다면 최솟값 갱신
        if (cur == targetWeak.length && distIdx < answer) answer = distIdx;
    }
}