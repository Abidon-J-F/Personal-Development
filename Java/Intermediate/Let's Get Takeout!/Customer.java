/*
This is part of Let's Get Takeout! program.
Author: Abidon Jude Fernandes
Date: 11/2023-12/2023
*/

public class Customer {
    private String name;
    private int money;

    public Customer(String name, int money) {
        this.name = name;
        this.money = money;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getMoney() {
        return this.money;
    }

    public void setMoney(int money) {
        this.money = money;
    }
}
