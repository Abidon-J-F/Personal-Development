 /*
  This is a Basic Mathematical Calculator program.
  Author: Abidon Jude Fernandes
  Date: 14/02/2022
  */
  
public class Calculator{
  
  public Calculator(){

  }
    // Integer constructor version
    public int add(int a, int b){
        return a + b;
      }
    public int subtract(int a, int b){
        return a - b;
      }
    public int multiply(int a, int b){
        return a * b;
      }
    public int divide(int a, int b){
        return a / b;
      }
    public int modulo(int a, int b){
        return a % b;
      }

    //Double constructor version
    public double addDouble(double a, double b){
        return a + b;
      }
    public double subtractDouble(double a, double b){
        return a - b;
      }
    public double multiplyDouble(double a, double b){
        return a * b;
      }
    public double divideDouble(double a, double b){
        return a / b;
      }
    public double moduloDouble(double a, double b){
        return a % b;
      }

      public static void main(String[] args){
      Calculator myCalculator = new Calculator();

      //Integer Answer Version
      System.out.println(myCalculator.add(5, 7));
      System.out.println(myCalculator.subtract(45, 11));
      System.out.println(myCalculator.multiply(3, 24));
      System.out.println(myCalculator.divide(22, 2));
      System.out.println(myCalculator.modulo(50, 6));
      
      System.out.println(" ");

      //Double Answer Version
      System.out.println(myCalculator.addDouble(5, 28));
      System.out.println(myCalculator.subtractDouble(45, 25));
      System.out.println(myCalculator.multiplyDouble(3, 15));
      System.out.println(myCalculator.divideDouble(22, 13));
      System.out.println(myCalculator.moduloDouble(50, 7));
      } 
}
