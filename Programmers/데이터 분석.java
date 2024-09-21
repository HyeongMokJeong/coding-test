import java.util.Arrays;
import java.util.Map;

class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        Map<String, Integer> indexMap = Map.of(
            "code", 0,
            "date", 1,
            "maximum", 2,
            "remain", 3
        );

        return Arrays.stream(data)
            .filter(d -> d[indexMap.get(ext)] < val_ext)
            .sorted((d1, d2) -> Integer.compare(d1[indexMap.get(sort_by)], d2[indexMap.get(sort_by)]))
            .toArray(int[][]::new);
    }
}