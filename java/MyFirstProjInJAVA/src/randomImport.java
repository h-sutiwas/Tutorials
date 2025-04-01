import java.util.Random;

public class randomImport {
    public static void main(String[] args) {
        Random random =  new Random();

        int number1;
        int number2;
        int number3;

        number1 = random.nextInt(1, 101);
        number2 = random.nextInt(1, 101);
        number3 = random.nextInt(1, 101);

        System.out.println(number1);

        double number;

        number = random.nextDouble();

        System.out.println(number);

        boolean isHeads;

        isHeads = random.nextBoolean();

        if (isHeads){
            System.out.println("HEADS");
        } else {
            System.out.println("TAILS");
        }
    }
}
