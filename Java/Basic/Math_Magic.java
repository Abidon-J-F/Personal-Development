  /*
  This is a Math Magic program. It outputs the integer three no matter what integer you insert into the variable.
  Author: Abidon Jude Fernandes
  Date: 31/01/2022
  */

public class Magic {
	public static void main(String[] args) {

    /* 
    This here is the original number.
    It should not contain a 0 
    */

int myNumber = 5;

    int stepOne = myNumber * myNumber;
    int stepTwo = stepOne + myNumber;
    int stepThree = stepTwo / myNumber;
    int stepFour = stepThree + 17;
    int stepFive = stepFour - myNumber;
    int stepSix = stepFive / 6;
    
    System.out.println(stepSix);
	}
}
