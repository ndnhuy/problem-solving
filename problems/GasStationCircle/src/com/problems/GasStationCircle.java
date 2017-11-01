package com.problems;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

/**
 * Created by huydnnguyen on 6/11/2017.
 */
public class GasStationCircle {
    public static class PetrolPump {
        int petrol;
        int distance;

        public PetrolPump(int p, int d) {
            petrol = p;
            distance = d;
        }
    }

    public static int findFirstPoint(PetrolPump[] pumps) {
        int startPoint = 0;
        int truckPetrol = pumps[startPoint].petrol;
        int i = startPoint;
        int end = -1;
        boolean visitedOnce = false;
        while (i != end) {
            if (end == -1) {
                end = startPoint;
            }

            if (i == pumps.length - 1) {
                visitedOnce = true;
            }

            int nextStop = (i + 1) % pumps.length;
            if (truckPetrol - pumps[i].distance < 0) {
                if (visitedOnce) {
                    return -1;
                }

                startPoint = nextStop;
                truckPetrol = pumps[startPoint].petrol;
                i = startPoint;
                continue;
            }

            truckPetrol = truckPetrol - pumps[i].distance + pumps[nextStop].petrol;
            i = nextStop;
        }

        return startPoint;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader r = new BufferedReader(new FileReader("D:\\projects\\sideprojects\\java-learning-projects\\src\\com\\problems\\GasStationCircle.txt"));

        int n = Integer.parseInt(r.readLine());
        PetrolPump[] pumps = new PetrolPump[n];
        for (int i = 0; i < n; i++) {
            String[] s = r.readLine().split(" ");
            PetrolPump p = new PetrolPump(Integer.parseInt(s[0]), Integer.parseInt(s[1]));
            pumps[i] = p;
        }

        System.out.println(findFirstPoint(pumps));
    }
}
