import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public String[] solution(String[] files) {
        Arrays.sort(files, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                String[] file1 = separationOfFile(o1);
                String[] file2 = separationOfFile(o2);
 
                int result = file1[0].compareTo(file2[0]);
 
                if (result == 0) {
                    int number1 = Integer.parseInt(validateNumber((file1[1])));
                    int number2 = Integer.parseInt(validateNumber((file2[1])));
                    return number1 - number2;
                }
                return result;
            }
        });
 
        return files;
    }
 
    private String[] separationOfFile(String file) {
        file = file.toLowerCase();
 
        // 숫자가 처음 나오는 부분을 기준으로 String 분리
        String head = file.split("[0-9]")[0];
        String number = file.substring(head.length());
        String[] separateFile = {head, number};
        return separateFile;
    }
 
    private String validateNumber(String number) {
        StringBuilder sb = new StringBuilder();
        for (char c : number.toCharArray()) {
            if (Character.isDigit(c) && sb.length() <= 5) {
                sb.append(c);
            } else {
                return sb.toString();
            }
        }
 
        return sb.toString();
    }
}