class Solution {
    private static int callCount = 0;
    private static int removeCount = 0;

    public int[] solution(String s) {
        run(s);
        return new int[]{callCount, removeCount};
    }

    private void run(String target) {
        if (target.equals("1")) return;
        callCount++;

        int beforeLength = target.length();

        int afterLength = target.replace("0", "").length();
        removeCount += beforeLength - afterLength;
        
        run(Integer.toBinaryString(afterLength));
    }
}