class Solution {
    public String solution(String m, String[] musicinfos) {
        m = changePoundKey(m);
        
        String answer = "(None)";
        int maxTime = Integer.MIN_VALUE;

        for (String target : musicinfos) {
            // 시간 동안의 모든 악보를 완성한다.
            String[] t = target.split(",");
            int gap = getTimeGap(t[0], t[1]);
            // 효율을 위해 시간이 더 적으면 건너뛴다.
            if (gap <= maxTime) continue;
            String title = t[2], music = changePoundKey(t[3]);
            int musicLength = music.length();
            
            StringBuilder sb = new StringBuilder();
            int idx = 0;
            while (sb.length() <= gap) {
                char pitch = music.charAt(idx++ % musicLength);
                sb.append(pitch);
            }
            
            // 악보 안에 m이 포함되어 있는지 확인한다.
            String fullMusic = sb.toString();
            
            if (fullMusic.contains(m)) {
                answer = title;
                maxTime = gap;
            }
        }

        return answer;
    }

    // # 음을 소문자로 변환
    private String changePoundKey(String target) {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < target.length() - 1; i++) {
            char t = target.charAt(i);
            if (t == '#') continue;
            char nextT = target.charAt(i + 1);

            if (nextT == '#') {
                sb.append(Character.toLowerCase(t));
            } else {
                sb.append(t);
            }
        }
        char lastT = target.charAt(target.length() - 1);
        if (lastT != '#') sb.append(lastT);
        return sb.toString();
    }

    // HH:MM 형식의 String 두 개의 차이 계산
    private int getTimeGap(String start, String end) {
        String[] sParts = start.split(":");
        String[] eParts = end.split(":");

        int sHour = Integer.parseInt(sParts[0]);
        int sMinutes = Integer.parseInt(sParts[1]);
        int eHours = Integer.parseInt(eParts[0]);
        int eMinutes = Integer.parseInt(eParts[1]);

        return (eHours * 60 + eMinutes) - (sHour * 60 + sMinutes);
    }
}