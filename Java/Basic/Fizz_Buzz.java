 /*
  This is a FizzBuzz program.
  Author: Abidon Jude Fernandes
  Date: 17/03/2022
  */

class FizzBuzz {

    public static void main(String[] args) {
        
        for (int i = 0; i <= 100; i++) {
          if (i % 3 == 0 && i % 5 == 0){
           System.out.println("FizzBuzz");           
          } else if (i % 3 == 0) {
           System.out.println("Fizz");           
          } else if (i % 5 == 0){
           System.out.println("Buzz");           
          } else {
           System.out.println(i);           
          }
        }

    }

}
