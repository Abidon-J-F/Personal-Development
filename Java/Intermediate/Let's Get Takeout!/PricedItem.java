/*
This is part of Let's Get Takeout! program.
Author: Abidon Jude Fernandes
Date: 11/2023-12/2023
*/

public interface PricedItem<T extends Number> {
    T getPrice();

    void setPrice(T price);
}
