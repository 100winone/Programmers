public class LV1_3 {
    public static void main(String[] args) {
        String day = "";
        day = solution(5, 24);
        System.out.println(day);
    }
    public static String solution(int a, int b){
        String answer = "";
        a -= 1;
        b -= 1;
        String [] year = new String[366];
        String [] day = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
        int picked_day = 0;
        int [] month = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        for (int i = 0; i < year.length; i++){
            year[i] = day[(i + 5) % 7];
        }
        for (int i = 0; i < a; i ++){
            picked_day += month[i];
        }
        picked_day += b;
        answer = year[picked_day];
        return answer;
    }
}
