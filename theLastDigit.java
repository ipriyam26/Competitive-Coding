
import java.util.Scanner;
public class theLastDigit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int test_cases = sc.nextInt();
        for (int i = 0; i < test_cases; i++) {
            int a = sc.nextInt();
            String b = sc.next(); 
            int res = 0;
            for (int j = 0; j < b.length(); j++) {
                res = (res*10 + (int)b.charAt(j)-'0')%5;
            }
           
                System.out.println((int)Math.pow(a, res)%10);
            // }
        }

    }
}