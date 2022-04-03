import java.util.Locale;
import java.util.Scanner;

public class BankAccount {
    private String name;
    public int accountNumber;
    public int balance;

    public BankAccount(String name, int accountNumber, int balance) {
        this.name = name.toUpperCase(Locale.ROOT);
        this.accountNumber = accountNumber;
        this.balance = balance;
    }

    public void deposit() {
        System.out.println("Please enter the amount you wish to deposit: " + "\n--");
        Scanner scan = new Scanner(System.in);
        int amount = scan.nextInt();
        if (amount > 10000) {
            System.out.println("Unable to process request, deposit cannot exceed 10000");
            deposit();
        } else {
            System.out.println("Depositing amount: " + amount + "\n--");
            balance += amount;
            System.out.println(name +"'s new balance is " + balance + "\n--");
        }
    }

    public void withdraw() {
        System.out.println("Please enter the amount you wish to withdraw: " + "\n--");
        Scanner scan = new Scanner(System.in);
        int amount = scan.nextInt();
        if (amount > balance) {
            System.out.println("Unable to process request, insufficient balance" + "\n--");
            withdraw();
        } else {
            System.out.println("Withdrawing amount: " + amount + "\n--");
            balance = balance - amount;
            System.out.println(name +"'s new balance is " + balance + "\n--");
        }
    }

    public String toString() {
        return String.format(name + " " + accountNumber + " " + balance);
    }
}
