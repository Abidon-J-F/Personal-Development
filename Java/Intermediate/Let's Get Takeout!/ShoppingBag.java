/*
This is part of Let's Get Takeout! program.
Author: Abidon Jude Fernandes
Date: 11/2023-12/2023
*/

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;

public class ShoppingBag <T extends PricedItem <Integer> > {
    private Map<T,Integer> shoppingBag;

    // Constructor
    public ShoppingBag() {

        this.shoppingBag = new HashMap<>();
    }

    public void addItem(T item){


        int acumulador = 0;
        if (!shoppingBag.containsKey(item)){
            if (!shoppingBag.isEmpty()) {
                shoppingBag.put(item, acumulador += 1);
                System.out.println(acumulador);
            } else {
                shoppingBag.put(item, acumulador = 1);
                System.out.println(acumulador);
            }
        }

    }

    public int getTotalPrice(){

        int totalPrice = 0;

        for (Map.Entry<T, Integer> eachPair : shoppingBag.entrySet() ){

            totalPrice += eachPair.getKey().getPrice() * eachPair.getValue();
        }
        return totalPrice;
    }
}
