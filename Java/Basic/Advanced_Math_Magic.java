  /*
  This is a Advanced Math Magic program which outputs the number three no matter what number you insert into the variable.
  Author: Abidon Jude Fernandes
  Date: 06/02/2022
  */

public class Magic {
	public static void main(String[] args) {

    /* 
    This here is the original number.
    It should not contain a 0 
    */

    int myNumber = 57;

    int magicNumber = myNumber * myNumber;
    magicNumber += myNumber;
    magicNumber /= myNumber;
    magicNumber += 17;
    magicNumber -= myNumber;
    magicNumber /= 6;
    
    System.out.println(magicNumber);  

	}
}