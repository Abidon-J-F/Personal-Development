/*
This is part of the Medieval Serialization program.
Author: Abidon Jude Fernandes
Date: 09/2023-10/2023
*/

import java.io.Serializable;

public class Weapon implements Serializable {

    private final static long serialVersionUID = 1L;
    private final String name;
    private  final int damage;

    // Constructor
    public Weapon(String name, int damage){
        this.name = name;
        this.damage = damage;
    }

    // Getters & Setters
    public String getName() {
        return name;
    }

    public int getDamage() {
        return damage;
    }
}
