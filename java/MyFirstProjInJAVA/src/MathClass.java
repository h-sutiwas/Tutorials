import java.util.Scanner;

public class MathClass {
    public static void main(String[] args) {

        // System.out.println(Math.PI);
        // System.out.println(Math.E);

        double result;

        result = Math.pow(2, 3);
        result = Math.abs(-5);
        result = Math.sqrt(9);
        result = Math.round(Math.PI);
        result = Math.ceil(Math.PI);
        result = Math.floor(Math.PI);

        System.out.println(result);

        Scanner scanner = new Scanner(System.in);

        double a;
        double b;
        double c;

        System.out.print("Enter the length odf side A: ");
        a = scanner.nextDouble();

        System.out.print("Enter the length odf side B: ");
        b = scanner.nextDouble();

        c = Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2));

        System.out.println("The hypotenuse (side c) is: " + c + "cm");

        double radius;
        double circumference;
        double area;
        double volume;

        System.out.print("Enter the radius: ");
        radius = scanner.nextDouble();

        circumference = 2 * Math.PI * radius;
        area = Math.PI * Math.pow(radius, 2);
        volume = (4.0 / 3.0) * Math.PI * Math.pow(radius, 3);


        // NUMLOCK + ALT + 0179 => power of 3 = ³
        System.out.printf("The circumference is: %.1fcm\n", circumference);
        System.out.printf("The area is: %.1fcm²\n", area);
        System.out.printf("The volume is: %.1fcm³\n" , volume);

        scanner.close();
    }
}
