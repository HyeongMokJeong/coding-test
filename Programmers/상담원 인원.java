import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

class Solution { 
    public int solution(int k, int n, int[][] reqs) {
        List<List<int[]>> q = init(k, reqs);
        // gap[1][2] = 1번 유형에 상담사 2명을 배치했을 때 총 대기시간
        int[][] gap = new int[k + 1][n - k + 1];

        for (int i = 0; i <= k; i++) calculate(gap[i], q.get(i));

        return getMinTimeGap(n - k, gap, 1);
    }

    private List<List<int[]>> init(int k, int[][] reqs) {
        List<List<int[]>> result = new ArrayList<>();
        for (int idx = 0; idx <= k; idx++) {
            result.add(new ArrayList<>());
        }
        for (int[] req : reqs) {
            int start = req[0];
            int end = start + req[1];
            int type = req[2];
            result.get(type).add(new int[] { start, end });
        }
        return result;
    }

    private void calculate(int[] gap, List<int[]> reqs) {
        for (int i = 0; i < gap.length; i++) {
            int maxPpl = i + 1; // 최대 상담원 수
            int count = 0; // 상담자 수
            int gapTotal = 0;

            PriorityQueue<Integer> endQ = new PriorityQueue<>();
            for (int[] time : reqs) {
                int s = time[0]; int e = time[1];

                // 현재 상담자 시작 시간에 이전 상담자들이 종료되었다면 제거
                while (!endQ.isEmpty() && s >= endQ.peek()) {
                    endQ.poll();
                    count--;
                }
                // 현재 상담자 시작 시점에 이전 상담자들이 상담중이면 카운트 추가
                if (endQ.isEmpty() || s < endQ.peek()) count++;
                // 만약 최대 상담원 수보다 상담자 수가 많다면 대기 시간 계산
                if (count > maxPpl) {
                    int g = endQ.poll() - s;
                    e += g;
                    gapTotal += g;
                    count --;
                }
                endQ.add(e);
            }
            gap[i] = gapTotal;
        }
    }

    private int getMinTimeGap(int maxPpl, int[][] gapTable, int type) {
        int minTotal = Integer.MAX_VALUE;
        for (int i = 0; i <= maxPpl; i++) {
            int value = gapTable[type][i];
            if (type < gapTable.length - 1) value += getMinTimeGap(maxPpl - i, gapTable, type + 1);
            minTotal = Math.min(minTotal, value);
        }
        return minTotal;
    }
}