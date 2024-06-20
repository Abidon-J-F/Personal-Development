/*
This is 2 of 2 main parts of the Medieval Serialization program.
Author: Abidon Jude Fernandes
Date: 09/2023-10/2023
*/

import java.io.*;
import java.util.Scanner;
import java.io.Serializable;

public class Player implements Serializable {

    private final static long serialVersionUID = 1L;
    private final String name;
    private double health;
    private Weapon currentWeapon;
    private Helmet helmet;
    private Shirt shirt;
    private Trouser trouser;
    private Shoe shoe;

    // Constructor
    public Player(String name){
        this.name = name;
        this.currentWeapon = new Weapon("Rusty Short Sword", 3);
        this.health = 100;
    }

    // Instance Methods
    public void takeDamage(double enemyAttack){
        double damage = enemyAttack - (helmet.getDefenseRating() / 5.0);
        this.health -= damage;

        if (this.health <= 0) {
            System.out.println("You have succumbed to the enemy, better luck next time.");
            System.exit(1);
        } else {
            System.out.println("Current health: " + this.health);
        }
    }

    public void heal(double healthToAdd){
        this.health += healthToAdd;
        if(this.health > 100) {
            this.health = 100;
        }
    }

    // Getters & Setters
    public String getName(){
        return name;
    }

    public String getCurrentWeapon(){
        return "Currently wielding: " + currentWeapon.getName() + ". This weapon does " + currentWeapon.getDamage() + " damage.\n";
    }

    public void setCurrentWeapon(Weapon currentWeapon) {
        this.currentWeapon = currentWeapon;
    }

    public double getHealth(){
        return health;
    }

    public int getDefenseRating(){
        return helmet.getDefenseRating() + shirt.getDefenseRating() + trouser.getDefenseRating() + shoe.getDefenseRating();
    }

    public Helmet getHelmet(){
        return helmet;
    }

    public void setHelmet(Helmet helmet) {
        this.helmet = helmet;
    }
    public Shirt getShirt() {
        return shirt;
    }

    public void setShirt(Shirt shirt){
        this.shirt = shirt;
    }

    public Trouser getTrouser() {
        return trouser;
    }

    public void setTrouser(Trouser trouser){
        this.trouser = trouser;
    }

    public Shoe getShoe() {
        return shoe;
    }

    public void setShoe(Shoe shoe) {
        this.shoe = shoe;
    }

    @Override
    public String toString(){
        return "\nCurrent Player: \n" +
                "Name: " + name + "\n" +
                "Health: " + getHealth() + "\n" +
                getCurrentWeapon() +
                "Equipped Armour: " + "\n" +
                "   Helmet: " + helmet +
                "   Shirt: " + shirt +
                "   Trousers: " + trouser +
                "   Shoes: " + shoe;
    }
}
