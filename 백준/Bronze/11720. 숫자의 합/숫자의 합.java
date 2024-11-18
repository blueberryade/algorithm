import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String str = sc.next();
        
        char[] chars = str.toCharArray();
        int sum = 0;
        for (int i = 0; i < chars.length ; i++) {
            sum+=chars[i]-'0'; 
        }

        System.out.println(sum);
    }
}