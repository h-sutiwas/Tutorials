import java.util.Scanner;

public class CompoundInterestCalculator {
    public static void main(String[] args) {
        // Compound Interest Calculator

        Scanner scanner = new Scanner(System.in);

        double principle;
        double rate;
        int timesCompound;
        int years;
        double amount;

        System.out.print("Enter the principal amount: ");
        principle = scanner.nextDouble();

        System.out.print("Enter the interest rate (in %): ");
        rate = scanner.nextDouble() / 100;

        System.out.print("Enter the number of time compounded per year: ");
        timesCompound = scanner.nextInt();

        System.out.print("Enter the number of years: ");
        years = scanner.nextInt();

        amount = principle * Math.pow(1 + rate / timesCompound, timesCompound * years);

        System.out.printf("The amount after %d years is: $%.2f", years, amount);

        scanner.close();
    }
}
