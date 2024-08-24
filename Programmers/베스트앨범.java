import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        List<Integer> answer = new ArrayList<>();

        // 각 장르 별 재생횟수 총합 map
        Map<String, Integer> countMap = new HashMap<>();

        // 각 장르 별 [ 재생횟수, 인덱스 ] 최대 힙
        Map<String, PriorityQueue<int[]>> playMap = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            countMap.put(genres[i], countMap.getOrDefault(genres[i], 0) + plays[i]);
            playMap.putIfAbsent(genres[i], new PriorityQueue<>((o1, o2) -> o2[0] - o1[0]));
            playMap.get(genres[i]).add(new int[]{plays[i], i});
        }

        List<String> genreList = new ArrayList<>();
        for (String k : countMap.keySet()) genreList.add(k);
        genreList.sort((o1, o2) -> countMap.get(o2) - countMap.get(o1));

        int size = 2;
        for (String g : genreList) {
            for (int i = 0; i < size; i++) {
                if (playMap.get(g).isEmpty()) break;
                answer.add(playMap.get(g).poll()[1]);
            }
        }

        return answer.stream().mapToInt(i -> i).toArray();
    }
}