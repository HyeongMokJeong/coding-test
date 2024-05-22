import java.util.ArrayDeque;
import java.util.List;
import java.util.Queue;

class Solution {
    class Block {
        private int x;
        private int y;
        private String moveString;

        public Block(int x, int y, String moveString) {
            this.x = x;
            this.y = y;
            this.moveString = moveString;
        }

        public Block down() {
            return new Block(x + 1, y, moveString + "d");
        }

        public Block left() {
            return new Block(x, y - 1, moveString + "l");
        }

        public Block right() {
            return new Block(x, y + 1,  moveString + "r");
        }

        public Block up() {
            return new Block(x - 1, y, moveString + "u");
        }
    }

    public String solution(int n, int m, int x, int y, int r, int c, int k) {
        Queue<Block> queue = new ArrayDeque<>(List.of(new Block(x, y, "")));

        while (!queue.isEmpty()) {
            Block target = queue.poll();
            int tx = target.x; int ty = target.y; int tc = target.moveString.length();

            if (tx == r && ty == c && tc == k) return target.moveString;
            
            if ((0 < tx + 1 && tx + 1 <= n) && (0 < ty && ty <= m) && tc + 1 <= k) queue.add(target.down());
            if ((0 < tx && tx <= n) && (0 < ty - 1 && ty - 1 <= m) && tc + 1 <= k) queue.add(target.left());
            if ((0 < tx && tx <= n) && (0 < ty + 1 && ty + 1 <= m) && tc + 1 <= k) queue.add(target.right());
            if ((0 < tx - 1 && tx - 1 <= n) && (0 < ty && ty <= m) && tc + 1 <= k) queue.add(target.up());
        }

        return "impossible";
    }
}