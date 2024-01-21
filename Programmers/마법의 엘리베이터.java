class Solution {
    public int solution(int storey) {
        int answer = 0;

        while (storey > 0) {
            // 1의 자리 수
            int digit = storey % 10;
            storey /= 10;

            // 만약 1의 자리가 5라면, 10의 자리수를 볼 필요가 있음
            if (digit == 5) {
                // 5x 이상이라면 100을 만들기 위해 더해줌
                if (storey % 10 >= 5) {
                    answer = answer + (10 - digit);
                    storey++;
                }
                // 4x 이하라면 10을 만들기 위해 빼줌
                else {
                    answer = answer + digit;
                }
            }
            // 6 ~ 9 라면, 1씩 더해서 10을 만들기 위해 10 - digit번의 이동 필요
            else if (digit > 5) {
                answer = answer + (10 - digit);
                storey++;
            }
            // 1 ~ 4 라면, 1씩 빼서 0을 만들기 위해 digit번의 이동 필요
            else {
                answer = answer + digit;
            }
        }
        return answer;
    }
}