class Solution {
    public long[] solution(long[] numbers) {
        long[] answer = new long[numbers.length];

        for (int i = 0; i < numbers.length; i++) {
            long target = numbers[i];
            String binaryTarget = Long.toBinaryString(target);

            if (target % 2 == 0) {
                answer[i] = target + 1;
            } else {
                int idx = binaryTarget.lastIndexOf("0");

                if (idx == -1) {
                    answer[i] = Long.parseLong(
                        "10" + binaryTarget.substring(1, binaryTarget.length()), 
                        2
                        );
                } else {
                    answer[i] = Long.parseLong(
                        binaryTarget.substring(0, idx) + "10" + binaryTarget.substring(idx + 2, binaryTarget.length()),
                        2
                    );
                }
            }
        }
        return answer;
    }
}