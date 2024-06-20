/*
This is part of the Threading in the Gym program.
Author: Abidon Jude Fernandes
Date: 02/2024-03/2024
*/

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Member {
    private final int id;

    public Member(int id) {
        this.id = id;
    }

    public int getId() {
        return this.id;
    }

    public List<Exercise> generateRoutine() {
        return IntStream.range(0, 6).mapToObj(_i -> new Exercise()).collect(Collectors.toList());
    }

    public void performRoutine() throws InterruptedException {
        List<Exercise> routine = generateRoutine();

        routine.forEach(exercise -> {
            System.out.println("Gym Member " + this.getId() + " performing exercise: " + exercise);
            try {
                Thread.sleep(exercise.getDuration());
            } catch (InterruptedException e) {
                System.out.println(e);
            }
        });
    }
}
