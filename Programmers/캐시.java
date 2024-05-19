import java.util.LinkedList;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        LinkedList<String> queue = new LinkedList<>();
        if (cacheSize == 0) return cities.length * 5;

        for (String city : cities) {
            city = city.toLowerCase();
            if (queue.contains(city)) {
                answer += 1;
                queue.remove(city);
                queue.add(city);
            }
            else {
                answer += 5;
                if (queue.size() >= cacheSize) queue.remove(0);              
                queue.add(city);
            }
        }
        return answer;
    }
}