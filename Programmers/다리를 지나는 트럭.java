import java.util.Deque;
import java.util.ArrayDeque;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;

        Deque<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < bridge_length; i++) q.add(0);

        int weightIdx = 0, weightTemp = 0;
        while (weightIdx < truck_weights.length) {
            weightTemp -= q.poll();
            int target = truck_weights[weightIdx];

            if (weightTemp + target <= weight) {
                q.add(target);
                weightTemp += target;
                weightIdx += 1;
            } else {
                q.add(0);
            }
            answer += 1;
        }

        return answer + bridge_length;
    }
}