import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.ThreadLocalRandom;
import java.util.stream.IntStream;

public class WeightRandomNumber {
    public static void main(String[] args) {
        int[] w = new int[3];
        w[0] = 50;
        w[1] = 30;
        w[2] = 60;

        Map<Integer, Long> countByNum = new HashMap<>();
        for (int i = 0; i < 280; i++) {
            int version = f(w);
            countByNum.put(version, countByNum.getOrDefault(version, 0L) + 1);
        }

        System.out.println(countByNum);
    }

    public static int f(int[] w) {
        int[] clonedW = Arrays.copyOf(w, w.length);
        for (int i = 0; i < clonedW.length; i++) {
            if (i - 1 < 0) {
                continue;
            }
            clonedW[i] = clonedW[i - 1] + clonedW[i];
        }

        int sumOfWeight = IntStream.of(w).sum();
        int randomWeight = ThreadLocalRandom.current().nextInt(sumOfWeight + 1);
        for (int i = 0; i < clonedW.length; i++) {
            if (clonedW[i] > randomWeight) {
                return i;
            }
        }
        return clonedW.length - 1;
    }
}