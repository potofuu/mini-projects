import java.util.Scanner;

public class Banking {
    public static void main(String[] args) {
        System.out.println("--Banking--\n");
        System.out.println("Please enter your name below: \n--");
        Scanner scan = new Scanner(System.in);
        String name = scan.nextLine();
        BankAccount customer = new BankAccount(name, 0, 0);
        System.out.println("--\nWelcome to Banking " + name + "!");
        System.out.println("Please select an action:" + "\n--");
        System.out.println("A: Display Bank Info\n--");
        System.out.println("B: Deposit\n--");
        System.out.println("C: Withdraw\n--");
        System.out.println("D: Exit System\n--");
        String action = scan.nextLine();
        switch(action) {
            case "A":
                System.out.println("Display Test");
                break;
            case "B":
                System.out.println("Deposit Test");
                break;
            case "C":
                System.out.println("Withdraw Test");
                break;
            case "D":
                System.out.println("Exiting Sytem...\n--");
                break;
            default:
                System.out.println("Invalid Action");
        }
    }
}
