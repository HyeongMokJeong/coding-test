class Solution {
    public int[] solution(long[] numbers) {
        int[] answer = new int[numbers.length];
        
        for (int i = 0; i < numbers.length; i++) {
            String binary = Long.toBinaryString(numbers[i]);
            
            // 타겟을 2진수로 변환하고 포화 이진트리를 만든다. (포화 이진트리의 노드 개수 = 2 ** h - 1)
            // 2진수에서 오른쪽에 0을 추가하면 무시되므로, 왼쪽에만 붙인다.
            int h = 0;
            while((int) Math.pow(2, h) - 1 < binary.length()) h++;
        	while((int) Math.pow(2, h) - 1 != binary.length()) binary = "0" + binary;
        	
            answer[i] = check(binary);
        }
        return answer;
    }
    
    private int check(String target) {
        int mid = (target.length() - 1) / 2;
        char root = target.charAt(mid);
        String left = target.substring(0, mid);
        String right = target.substring(mid + 1, target.length());
        
        // 자식이 있는데 부모가 0이라면 표현할 수 없다.
        if (root == '0' && 
           (left.charAt((left.length() - 1) / 2) == '1' ||
           right.charAt((right.length() - 1) / 2) == '1')
           ) return 0;
        
        // 자식 트리가 리프 레벨이 아니라면 왼쪽, 오른쪽 재귀
        if (left.length() >= 3) {
            if (check(left) == 1 && check(right) == 1) return 1;
            else return 0;
        }
        // 리프 레벨이라면 항상 가능
        return 1;
    }
}