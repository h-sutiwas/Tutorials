import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // This is my first Java Program

        System.out.println("Hello and Welcome!!!\n");
        System.out.println("It's really good\n");
        System.out.println("Buy me pizza!");
        System.out.println("\n");

        // Variables
        // variable = a reusable container for a value
        //            a reusable behaves as if it was the value it contains

        // Primitive = simple value stored directly in memory (stack)
        // Reference = memory address (stack) that points to the (heap)

        // Primitive vs Reference
        // ---------    ---------
        // int          string
        // double       array
        // char         object
        // boolean

        // 2 Steps to create a variable
        // ----------------------------
        // 1. declaration
        // 2. assignment

        int age = 30;
        int year = 2025;
        int quantity = 1;

        double price = 19.99;
        double gpa = 3.5;
        double temperature = -12.5;

        char grade = 'A';
        char symbol = '!';
        char currency = '$';

        boolean isStudent = true;
        boolean forSale = false;
        boolean isOnline = true;

        String name = "Sutiwas Jitsopak";
        String food = "pizza";
        String email = "s.jitsopak@gmail.com";


        System.out.println("The year is " + year);

        System.out.println("$" + price);

        System.out.println(grade);

        System.out.println(isStudent);
        System.out.println("\n");

        System.out.println("My name is " + name);
        System.out.println("My email is " + email);
        System.out.println("My favorite food is " + food);
        System.out.println("I'm " + age + " years old.");
        System.out.println("My gpa is " + gpa);

        // 3. User Input from import scanner package
        // at the top of our Java file (basically before Main class)

        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter your name: ");
        String nameIn = scanner.nextLine();

        System.out.println("Hello " + nameIn);

        scanner.close();

        // If - statement
        if (isStudent){
            System.out.println("This person is a student\n");
        }
        else {
            System.out.println("This person is not a student");
        }


        // Loop
        // for (int i = 1; i <= 10; i++) {
        // System.out.println("i = " + i);
        // }
    }
}