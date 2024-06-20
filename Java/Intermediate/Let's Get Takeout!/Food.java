/*
This is part of Let's Get Takeout! program.
Author: Abidon Jude Fernandes
Date: 11/2023-12/2023
*/

public class Food implements PricedItem<Integer> {

    private String name;
    private String description;
    private int price;

    public Food(String name, String description, int price) {
        this.name = name;
        this.description = description;
        this.price = price;
    }

    public String getName() {
        return this.name;
    }

    @Override
    public Integer getPrice() {
        return this.price;
    }

    @Override
    public void setPrice(Integer price) {
        this.price = price;
    }



    @Override
    public String toString() {
        return String.format("\n %s: %s    Cost: %d\n", this.name, this.description, this.price);
    }
}
