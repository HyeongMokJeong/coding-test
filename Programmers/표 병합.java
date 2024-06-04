import java.util.ArrayList;
import java.util.List;

class Solution {
    int size = 50;
    Cell[][] table = initTable();

    class Cell {
        String value = null;
    }

    void merge(int x1, int y1, int x2, int y2) {
        Cell target = table[x1][y1];
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (table[i][j] == target) table[i][j] = table[x2][y2];
            }
        }
    }

    public String[] solution(String[] commands) {
        List<String> printList = new ArrayList<>();

        for (String command : commands) {
            String[] part = command.split(" ");

            switch (part[0]) {
                case "UPDATE":
                    if (part.length == 4) {
                        int r = Integer.valueOf(part[1]) - 1; int c = Integer.valueOf(part[2]) - 1;
                        table[r][c].value = part[3];
                    }
                    else {
                        String value1 = part[1]; String value2 = part[2];
                        for (int i = 0; i < size; i++) {
                            for (int j = 0; j < size; j++) {
                                if (table[i][j].value == value1) table[i][j].value = value2;
                            }
                        }
                    }
                    break;
                case "MERGE":
                    int r1 = Integer.valueOf(part[1]) - 1; int c1 = Integer.valueOf(part[2]) - 1;
                    int r2 = Integer.valueOf(part[3]) - 1; int c2 = Integer.valueOf(part[4]) - 1;

                    if (table[r1][c1] == table[r2][c2]) break;
                    if (table[r1][c1].value == null && table[r2][c2].value != null) merge(r1, c1, r2, c2);
                    else merge(r2, c2, r1, c1);
                    break;
                case "UNMERGE":
                    int mr = Integer.valueOf(part[1]) - 1; int mc = Integer.valueOf(part[2]) - 1;
                    Cell del = table[mr][mc];
                    for (int i = 0; i < size; i++) {
                        for (int j = 0; j < size; j++) {
                            if (table[i][j] == del) table[i][j] = new Cell();
                        }
                    }
                    if (del.value != null) table[mr][mc].value = del.value;
                    break;
                case "PRINT":
                    int r = Integer.valueOf(part[1]) - 1; int c = Integer.valueOf(part[2]) - 1;
                    printList.add((table[r][c].value == null) ? "EMPTY" : table[r][c].value);
                    break;
            }
        }
        return printList.toArray(new String[printList.size()]);
    }

    private Cell[][] initTable() {
        Cell[][] table = new Cell[size][size];

        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) table[i][j] = new Cell();
        }
        return table;
    }
}