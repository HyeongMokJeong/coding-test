import java.util.*;

class Solution {
    int answer = 0;
    char dummy = ' ';

    public int solution(int m, int n, String[] board) {
        char[][] charArray = new char[board.length][];
        for (int i = 0; i < board.length; i++) charArray[i] = board[i].toCharArray();

        while (remove(charArray)) move(charArray);
        
        return answer;
    }

    private boolean remove(char[][] board) { 
        Set<String> set = new HashSet<>();
        boolean flag = false;

        for (int i = 0; i < board.length - 1; i++) {
            for (int j = 0; j < board[0].length - 1; j++) {
                char target = board[i][j];
                if (target == dummy) continue;
                char right = board[i][j + 1];
                char down = board[i + 1][j];
                char opposite = board[i + 1][j + 1];

                if (target == right && target == down && target == opposite) {
                    flag = true;
                    set.addAll(List.of(
                        i + "," + j,
                        i + "," + (j + 1),
                        (i + 1) + "," + j,
                        (i + 1) + "," + (j + 1)
                    ));
                }
            }
        }

        for (String removeTarget : set) {
            String[] parts = removeTarget.split(",");
            board[Integer.parseInt(parts[0])][Integer.parseInt(parts[1])] = dummy;
            answer += 1;
        }

        return flag;
    }

    private void move(char[][] board) {
        for (int i = board.length - 2; i >= 0; i--) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i + 1][j] == dummy) {
                    int temp = 1;
                    while (temp + i + 1 < board.length && board[i + temp + 1][j] == dummy) temp += 1;

                    board[i + temp][j] = board[i][j];
                    board[i][j] = dummy;
                }
            }
        }
    }
}