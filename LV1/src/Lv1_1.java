/*
 * 20201021 두 개 뽑아서 더하기 LV1
 * */
import java.util.ArrayList;
import java.util.Arrays;

public class Lv1_1 {
    public static void main(String[] args) {

        int[] numbersA = {2, 1, 3, 4, 1};
        int[] numbersB = {5, 0, 2, 7};
        print(solution(numbersA));
        print(solution(numbersB));
    }
    public static void print(int[] numbers){
        for(int i = 0; i < numbers.length; i++){
            System.out.print(numbers[i] + " ");
        }
        System.out.println();
    }
    public static int[] solution(int[] numbers) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        int res = 0;
        for (int i = 0; i < numbers.length - 1; i++){
            for (int j = i + 1; j < numbers.length; j++){
                res = numbers[i] + numbers[j];
                if(!list.contains(res)){
                    list.add(res);
                }
            }
        }
        int[] answer = new int[list.size()];
        for(int i = 0; i < list.size(); i++){
            answer[i] = list.get(i);
        }
        Arrays.sort(answer);
        return answer;

    }
}
