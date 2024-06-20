/*
This is part of the Medieval Serialization program.
Author: Abidon Jude Fernandes
Date: 09/2023-10/2023
*/

import java.io.Serializable;

public class Trouser extends Armour implements Serializable {

    private final static long serialVersionUID = 1L;

    // Constructor
    public Trouser(String name, int durability, int defenseRating){
        super(name, durability, defenseRating);
    }
}
