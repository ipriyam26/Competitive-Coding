import java.util.Scanner;

/**
 * parking_lot
 */
// n = int(input())-3
// print(3*4**n*(8+3*n))
public class parking_lot {

public static long getPower(long a,int n){
long result = 1;

while (n>0) {

    if((n & 1)==1){
        result = result*a;
    }
    a = a*a;
    
    n = n >> 1;
    // System.out.println(a);
}
return result;
    
}


    public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt()-3;
    
    System.out.println(3*getPower(4, n)*(8+3*n));
    }
}