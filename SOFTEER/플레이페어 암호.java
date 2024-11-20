package SOFTEER;

import java.io.*;
import java.util.*;

class 플레이페어암호 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 1. 표 제작
        int graphSize = 5;
        String message = br.readLine();
        String key = br.readLine();
        // key에 포함되어 있는지를 판별할 visited 배열
        boolean[] visited = new boolean[26];
        char[][] graph = new char[graphSize][graphSize];
        // 각 알파벳의 좌표를 저장할 Map
        Map<Character, int[]> coordiMap = new HashMap<>();
        // graph를 초기화 하기위한 변수 x, y
        int x = 0; int y = 0;
        
        // Key를 순회하며 graph를 초기화한다.
        for (char k : key.toCharArray()) {
            int target = Integer.valueOf(k) - 'A';
            if (!visited[target]) {
                graph[x][y] = k;
                coordiMap.put(k, new int[]{x, y});
                visited[target] = true;
                y += 1;
                if (y >= graphSize) {
                    x += 1;
                    y = 0;
                }
            }
        }

        // key에 포함되지 않은 알파벳들을 순서대로 배치한다.
        for (int i = 0; i < visited.length; i++) {
            // * J는 제외해야 한다. *
            if (i == Integer.valueOf('J') - 'A') continue;
            if (!visited[i]) {
                if (x < graphSize && y < graphSize) {
                    char target = (char) (i + 65);
                    graph[x][y] = target;
                    coordiMap.put(target, new int[]{x, y});
                    y += 1;
                    if (y >= graphSize) {
                        x += 1;
                        y = 0;
                    }
                }
            }
        }

        // 2. 두 쌍으로 묶는다
        StringBuilder sb = new StringBuilder();
        sb.append(message);
		int idx = 0;
		while (idx < sb.length() - 1) {
			if (sb.charAt(idx) == sb.charAt(idx + 1)) {
				if (sb.charAt(idx) == 'X') sb.insert(idx + 1, 'Q');
				else sb.insert(idx + 1, 'X');
			}
			idx += 2;
		}
        if (sb.length() % 2 == 1) sb.append('X');

        // 3. 암호화
        idx = 0;
        while (idx < sb.length() - 1) {
			int[] aCoordi = coordiMap.get(sb.charAt(idx));
            int[] bCoordi = coordiMap.get(sb.charAt(idx + 1));

            // 같은 행
            if (aCoordi[0] == bCoordi[0]) {
                sb.setCharAt(idx, graph[aCoordi[0]][(aCoordi[1] + 1) % graphSize]);
                sb.setCharAt(idx + 1, graph[bCoordi[0]][(bCoordi[1] + 1) % graphSize]);
            } 
            // 같은 열
            else if (aCoordi[1] == bCoordi[1]) {
                sb.setCharAt(idx, graph[(aCoordi[0] + 1) % graphSize][aCoordi[1]]);
                sb.setCharAt(idx + 1, graph[(bCoordi[0] + 1) % graphSize][bCoordi[1]]);
            }
            // 서로 다른 행, 열에 존재하는 경우
            else {
                sb.setCharAt(idx, graph[aCoordi[0]][bCoordi[1]]);
                sb.setCharAt(idx + 1, graph[bCoordi[0]][aCoordi[1]]);
            }
			
			idx += 2;
		}
        System.out.println(sb.toString());
        br.close();
    }
}
