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
        System.out.println("Are you a student? (true/false): ");
        boolean isStudentIn = scanner.nextBoolean();
        scanner.nextLine(); // Add this line to consume the newline character

        if (isStudentIn) {
            System.out.println("--- STATUS CHECK STUDENT ---");
            System.out.println("------ PROCEED ONWARD ------");

            while (true) {

                System.out.println("Enter your name: ");
                String nameIn = scanner.nextLine();

                System.out.println("Enter your age: ");
                int ageIn = scanner.nextInt();
                scanner.nextLine(); // Add this line to consume the newline character

                System.out.println("Enter your gpa: ");
                double gpaIn = scanner.nextDouble();

                System.out.println("Hello " + nameIn);
                System.out.println("You are " + ageIn + " years old");
                System.out.println("Your GPA is: " + gpaIn);

                break;
            }
        } else {
            System.out.println("STATUS CHECK NOT STUDENT !!!!");
        }

        // Simple Area of RectangleInput
        double width = 0;
        double height = 0;
        double area = 0;

        Scanner scanner2 = new Scanner(System.in);
        System.out.println("Enter the width: ");
        width = scanner2.nextDouble();

        System.out.println("Enter the height: ");
        height = scanner2.nextDouble();

        area = height * width;

        // Windows: Numlock +  Alt + 0178
        // Mac: Start + spacebar
        System.out.println("The are is: " + area + "cm²");

        scanner2.close();


        // If - statement
        Scanner scanner3 = new Scanner(System.in);

        int ageIf;
        String nameIf;

        System.out.println("Enter your name: ");
        nameIf = scanner3.nextLine();

        System.out.println("Enter your age: ");
        ageIf = scanner3.nextInt();

        // GROUP 1
        if (nameIf.isEmpty()) {
            System.out.println("You didn't enter your name!😡");
        }
        else {
            System.out.println("Hello " + nameIf + "!👋");
        }


        // GROUP 2
        if (ageIf >= 65){
            System.out.println("You are a senior!👴");
        }
        else if(ageIf >= 18){
            System.out.println("You are an adult!👨");
        }
        else if(ageIf == 0){
            System.out.println("You are a baby!👶");
        }
        else if(ageIf < 0){
            System.out.println("You aren't even born yet!👼");
        }
        else {
            System.out.println("You are a minor!🧒");
        }

        // GROUP 3
        if (isStudent){
            System.out.println("This person is a student! 🧑‍🎓");
        }
        else {
            System.out.println("This person is NOT a student 🏢");
        }

        // Loop
        // for (int i = 1; i <= 10; i++) {
        // System.out.println("i = " + i);
        // }
    }
}