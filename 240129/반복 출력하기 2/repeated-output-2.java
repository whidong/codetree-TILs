import java.util.Scanner;

public class Main {       
    static void print(int a) {
        if(a == 0)
            return;
        print(a - 1);
        System.out.println("HelloWorld");
        }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int b = sc.nextInt();
        print(b);
    }
}